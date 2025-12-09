"""
encodings.py
-----------------
Utility helpers for explicit **bytes ⇔ str** conversions.

This revision adds *table‑driven* codecs so you can convert **without** relying
on Python’s implicit ``bytes(data)`` or ``str.encode/bytes.decode`` helpers.
A few widely used single‑byte encodings come pre‑loaded; others fall back
to the built‑in codecs (written in CPython).

Functions
~~~~~~~~~
- **normalize_encoding(enc)**          → canonical codec name.
- **to_str(data, encoding="utf-8")**    → smart decode (unchanged).
- **to_bytes(data, encoding="utf-8")**  → smart encode (unchanged).
- **to_str_explicit(...)** / **to_bytes_explicit(...)**
  Table‑driven conversions that *never* call ``decode`` / ``encode`` unless no
  map is available.
- **available_encodings()**            → runtime codec list.

The explicit helpers use frozen mapping tables (``MappingProxyType``) built from
CPython’s own *decoding_table* definitions in the ``encodings`` package.  This
keeps the implementation pure Python yet 100 % standards‑compliant.
"""

from __future__ import annotations

import importlib
import encodings.aliases
from types import MappingProxyType
from typing import Union, Mapping, Optional

# ---------------------------------------------------------------------------
# Alias → Canonical mapping
# ---------------------------------------------------------------------------
_ENCODING_ALIASES: dict[str, str] = {
    "utf8": "utf-8",
    "utf16": "utf-16",
    "utf32": "utf-32",
    "latin1": "latin-1",
    "latin_1": "latin-1",
    "iso88591": "iso8859-1",
    "cp1252": "cp1252",
    "shiftjis": "shift_jis",
    "sjis": "shift_jis",
    "cp1251": "cp1251",
    "windows1251": "cp1251",
    "gbk": "gbk",
    "big5": "big5",
}


def normalize_encoding(enc: str) -> str:
    """Return a canonical Python codec name for *enc*."""
    if not enc:
        raise ValueError("encoding name must be non-empty")
    key = enc.replace("-", "").replace("_", "").lower()
    return _ENCODING_ALIASES.get(key, enc)


# ---------------------------------------------------------------------------
# Build **explicit** single‑byte mapping tables from CPython codec modules
# ---------------------------------------------------------------------------

_SINGLE_BYTE_ENCODINGS = [
    "ascii",       # 7‑bit subset
    "latin-1",     # ISO‑8859‑1; identical byte-code‑point mapping
    "iso8859-2",   # Central/Eastern European (Latin‑2)
    "cp1251",      # Cyrillic Windows
    "cp1252",      # Western Windows
]


def _load_decoding_map(encoding: str) -> Mapping[int, str]:
    """Return *immutable* mapping {byte:int→char:str}; empty if unavailable."""
    try:
        mod = importlib.import_module(f"encodings.{encoding.replace('-', '_')}")
    except ModuleNotFoundError:
        return MappingProxyType({})

    table: Optional[str] = getattr(mod, "decoding_table", None)
    if not table:  # Could be e.g. a multibyte codec
        return MappingProxyType({})

    # Build dictionary once, expose as read‑only
    return MappingProxyType(
        {i: ch for i, ch in enumerate(table) if ch != "\ufffe"})


_ENCODING_MAPS: dict[str, Mapping[int, str]] = {
    enc: _load_decoding_map(enc) for enc in _SINGLE_BYTE_ENCODINGS
}

# Reverse maps for encoding (char - byte)
_ENCODING_REVERSE_MAPS: dict[str, Mapping[str, int]] = {
    enc: MappingProxyType({ch: b for b, ch in mapping.items()})
    for enc, mapping in _ENCODING_MAPS.items() if mapping
}


# ---------------------------------------------------------------------------
# Explicit *table‑driven* decode / encode helpers
# ---------------------------------------------------------------------------

def _charmap_decode(
        data: bytes | bytearray | memoryview,
        enc: str, errors: str) -> str:
    mapping = _ENCODING_MAPS.get(enc)
    if not mapping:  # Fallback to builtin if we don’t have a table
        print("no suitable mapping found, trying python's converter")
        return bytes(data).decode(enc, errors)

    chars: list[str] = []
    for idx, b in enumerate(bytes(data)):
        ch = mapping.get(b)
        if ch is not None:
            chars.append(ch)
            continue
        # Undefined byte handling
        if errors == "strict":
            raise UnicodeDecodeError(
                "charmap", bytes(data), idx, idx + 1, "invalid byte")
        elif errors == "replace":
            chars.append("\uFFFD")  # replacement char
        elif errors == "ignore":
            continue
        else:
            raise ValueError(f"unsupported errors handler: {errors!r}")
    return "".join(chars)


def _charmap_encode(text: str, enc: str, errors: str) -> bytes:
    rmap = _ENCODING_REVERSE_MAPS.get(enc)
    if not rmap:
        print("no suitable mapping found, trying python's converter")
        return text.encode(enc, errors)

    out = bytearray()
    for idx, ch in enumerate(text):
        bb = rmap.get(ch)
        if bb is not None:
            out.append(bb)
            continue
        if errors == "strict":
            raise UnicodeEncodeError(
                "charmap", text, idx, idx + 1, "character not in map")
        elif errors == "replace":
            out.append(ord("?"))
        elif errors == "ignore":
            continue
        else:
            raise ValueError(f"unsupported errors handler: {errors!r}")
    return bytes(out)


# Public API wrappers -------------------------------------------------------

def to_str_explicit(
    data: Union[str, bytes, bytearray, memoryview],
    encoding: str = "utf-8",
    errors: str = "strict",
) -> str:
    """Decode using our explicit charmap when available (see docs)."""
    if isinstance(data, str):
        return data
    if not isinstance(data, (bytes, bytearray, memoryview)):
        raise TypeError("data must be str or bytes-like")
    enc = normalize_encoding(encoding)
    return _charmap_decode(data, enc, errors)


def to_bytes_explicit(
    data: Union[str, bytes, bytearray],
    encoding: str = "utf-8",
    errors: str = "strict",
) -> bytes:
    """Encode using our explicit charmap when available (see docs)."""
    if isinstance(data, (bytes, bytearray)):
        return bytes(data)
    if not isinstance(data, str):
        raise TypeError("data must be str or bytes-like")
    enc = normalize_encoding(encoding)
    return _charmap_encode(data, enc, errors)


# ---------------------------------------------------------------------------
# Back‑compat convenience wrappers (unchanged behaviour)
# ---------------------------------------------------------------------------

def to_str(
    data: Union[str, bytes, bytearray, memoryview],
    encoding: str = "utf-8",
    errors: str = "strict",
) -> str:
    """Back‑compat: thin wrapper around builtin decode."""
    if isinstance(data, str):
        return data
    if not isinstance(data, (bytes, bytearray, memoryview)):
        raise TypeError(
            "Expected bytes-like object or str, got " + type(data).__name__)
    enc = normalize_encoding(encoding)
    return bytes(data).decode(enc, errors)


def to_bytes(
    data: Union[str, bytes, bytearray],
    encoding: str = "utf-8",
    errors: str = "strict",
) -> bytes:
    """Back‑compat: thin wrapper around builtin encode."""
    if isinstance(data, (bytes, bytearray)):
        return bytes(data)
    if not isinstance(data, str):
        raise TypeError(
            "Expected str or bytes-like object, got " + type(data).__name__)
    enc = normalize_encoding(encoding)
    return data.encode(enc, errors)


# ---------------------------------------------------------------------------
# Misc helpers
# ---------------------------------------------------------------------------

def available_encodings() -> list[str]:
    """Return **sorted** unique codec names available in this runtime."""
    return sorted(set(encodings.aliases.aliases.values()))


_HEX_CHARS = "0123456789abcdef"
_HEX_TO_INT = {
    f"{a}{b}": (i << 4) + j
    for i, a in enumerate(_HEX_CHARS) for j, b in enumerate(_HEX_CHARS)
}


def bytes_to_hex(data: bytes | bytearray | memoryview) -> str:
    """
    Convert binary data to a hex string
    (e.g. b'\x01\x02' → '0102') without using built-in .hex().
    """
    if not isinstance(data, (bytes, bytearray, memoryview)):
        raise TypeError("Expected bytes-like object")

    result: list[str] = []
    for b in data:
        high = _HEX_CHARS[(b >> 4) & 0x0F]
        low = _HEX_CHARS[b & 0x0F]
        result.append(high)
        result.append(low)
    return ''.join(result)


def hex_to_bytes(hex_str: str) -> bytes:
    """
    Convert a hex string to bytes
    (e.g. '0102' → b'\x01\x02') without using fromhex().
    """
    if not isinstance(hex_str, str):
        raise TypeError("Expected str")

    hex_str = hex_str.strip().replace(" ", "").lower()
    if len(hex_str) % 2 != 0:
        raise ValueError("Hex string must contain even number of digits")

    out = bytearray()
    for i in range(0, len(hex_str), 2):
        pair = hex_str[i:i+2]
        if pair not in _HEX_TO_INT:
            raise ValueError(f"Invalid hex byte: '{pair}'")
        out.append(_HEX_TO_INT[pair])
    return bytes(out)


__all__ = [
    "normalize_encoding",
    "to_str",
    "to_bytes",
    "to_str_explicit",
    "to_bytes_explicit",
    "available_encodings",
    "bytes_to_hex",
    "hex_to_bytes",
]
