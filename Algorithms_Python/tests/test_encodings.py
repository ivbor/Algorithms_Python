import pytest

from Algorithms_Python.encodings import (
    _ENCODING_MAPS, _ENCODING_REVERSE_MAPS, to_str_explicit,
    to_bytes_explicit
)


@pytest.mark.parametrize("encoding", list(_ENCODING_MAPS.keys()))
def test_single_byte_roundtrip(encoding: str):
    """Every byte maps to its char and back again under strict mode."""
    fmap = _ENCODING_MAPS[encoding]
    for byte_val, ch in fmap.items():
        if ch == "\ufffe":  # undefined placeholder
            continue
        # decode
        decoded = to_str_explicit(bytes([byte_val]), encoding)
        assert decoded == ch
        # encode (only if reversible)
        if ch in _ENCODING_REVERSE_MAPS[encoding]:
            encoded = to_bytes_explicit(ch, encoding)
            assert encoded == bytes([byte_val])

    sample = "zażółć gęślą jaźń – € αβγ"
    b = to_bytes_explicit(sample, "utf-8")
    s = to_str_explicit(b, "utf-8")
    assert s == sample
