import pytest

from Algorithms_Python.encodings import (
    _ENCODING_MAPS, _ENCODING_REVERSE_MAPS, to_str_explicit,
    to_bytes_explicit, to_str, to_bytes, bytes_to_hex, hex_to_bytes
)

SAMPLE = "zażółć gęślą jaźń – € αβγ"


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


def test_decode_error_handlers():
    data = b'a\xffb'

    with pytest.raises(UnicodeDecodeError):
        to_str_explicit(data, "ascii", errors='strict')

    assert to_str_explicit(data, "ascii", errors='replace') == 'a\uFFFDb'
    assert to_str_explicit(data, "ascii", errors='ignore') == 'ab'

    with pytest.raises(ValueError):
        to_str_explicit(data, "ascii", errors='unknown')


def test_encode_error_handlers():
    text = 'a\uFFFFb'

    with pytest.raises(UnicodeEncodeError):
        to_bytes_explicit(text, "cp1251", errors='strict')

    assert to_bytes_explicit(text, "cp1251", errors='replace') == b'a?b'
    assert to_bytes_explicit(text, "cp1251", errors='ignore') == b'ab'

    with pytest.raises(ValueError):
        to_bytes_explicit(text, "cp1251", errors='unknown')


def test_explicit_converters_raise_without_mapping():
    with pytest.raises(LookupError):
        to_str_explicit(SAMPLE.encode('utf-8'), "utf-8")

    with pytest.raises(LookupError):
        to_bytes_explicit(SAMPLE, "utf-8")


@pytest.mark.parametrize("datatype, func",
                         ((bytes, to_str),
                          (str, to_bytes)))
def test_raises_exceptions_for_python_wrappers(datatype, func):
    sample = SAMPLE if datatype == str else SAMPLE.encode('utf-8')
    with pytest.raises(ValueError):
        func(sample, encoding=None)


@pytest.mark.parametrize("datatype, func",
                         ((bytes, to_str_explicit),
                          (str, to_bytes_explicit)))
def test_raises_exceptions_for_explicit_functions_defaults(datatype, func):
    sample = SAMPLE if datatype == str else SAMPLE.encode('utf-8')
    with pytest.raises(ValueError):
        func(sample, encoding=None)


@pytest.mark.parametrize("data, expected",
                         ((b'\x00\x01\x0f\x10\xff', '00010f10ff'),
                          (bytearray(b'\xab\xcd'), 'abcd'),
                          (memoryview(b'\x7f\x80'), '7f80')))
def test_bytes_to_hex(data, expected):
    assert bytes_to_hex(data) == expected


@pytest.mark.parametrize("hex_str, expected",
                         (('00010f10ff', b'\x00\x01\x0f\x10\xff'),
                          ('ab cd', b'\xab\xcd'),
                          ('7F80', b'\x7f\x80')))
def test_hex_to_bytes(hex_str, expected):
    assert hex_to_bytes(hex_str) == expected


def test_hex_helpers_raise_on_invalid_input():
    with pytest.raises(TypeError):
        bytes_to_hex("00")

    with pytest.raises(TypeError):
        hex_to_bytes(b'\x00')

    with pytest.raises(ValueError):
        hex_to_bytes("abc")

    with pytest.raises(ValueError):
        hex_to_bytes("00gg")


def _hex_array(hex_str):
    compact = hex_str.replace(" ", "").lower()
    return [f"0x{compact[i:i + 2]}" for i in range(0, len(compact), 2)]


def _escaped_text(text):
    return text.encode("unicode_escape").decode("ascii")


def test_hex_bytes_string_bytes_hex_roundtrip(capsys):
    source_hex = "00 41 7f 80 ff"
    decoded_bytes = hex_to_bytes(source_hex)
    decoded_text = to_str_explicit(decoded_bytes, "latin-1")
    encoded_bytes = to_bytes_explicit(decoded_text, "latin-1")
    result_hex = bytes_to_hex(encoded_bytes)

    transitions = [
        f"hex: {_hex_array(source_hex)}",
        f"hex -> bytes: {decoded_bytes!r}",
        f"bytes -> string: {_escaped_text(decoded_text)}",
        f"string -> bytes: {encoded_bytes!r}",
        f"bytes -> hex: {_hex_array(result_hex)}",
    ]

    with capsys.disabled():
        for transition in transitions:
            print(transition)

    assert decoded_bytes == b'\x00A\x7f\x80\xff'
    assert decoded_text == '\x00A\x7f\x80\xff'
    assert encoded_bytes == decoded_bytes
    assert result_hex == source_hex.replace(" ", "")
