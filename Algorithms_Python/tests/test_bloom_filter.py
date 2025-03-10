import pytest
from Algorithms_Python.bloom_filter import Bloom_filter


def test_can_create_bloom_filter():
    bf = Bloom_filter()
    assert isinstance(bf, Bloom_filter)


@pytest.fixture
def bf():
    bf = Bloom_filter()
    return bf


@pytest.fixture
def bf_jenkins():
    bf = Bloom_filter(hashfunc='jenkins')
    return bf


def test_can_add_to_bloom_filter(bf):
    fails_count = 0
    for i in range(1000):
        bf.add(i)
        if not bf.check(i):
            fails_count += 1
    assert fails_count < 60, 'fails_count does not converge to 50'


def test_can_create_bloom_filter_jenkins(bf_jenkins):
    fails_count = 0
    for i in range(1000):
        bf_jenkins.add(i)
        if not bf_jenkins.check(i):
            fails_count += 1
    assert fails_count < 60, 'fails_count does not converge to 50'


def test_false_positives_less_than_5_percent(bf):
    fails_count = 0
    for i in range(10000):
        bf.add(i)
    for i in range(10000, 20000):
        if bf.check(i):
            fails_count += 1
    assert fails_count <= 500, \
        'fails exceed required range'

# make a distinct file with this test


def test_bloom_filter_stress():
    bf = Bloom_filter()
    fails_count = 0
    for i in range(10000):
        bf.add(i)
        if not bf.check(i):
            fails_count += 1
    assert fails_count < 50


def test_long_strings_for_advanced_jenkins(bf_jenkins):
    for i in range(1000):
        str_to_add = ''
        fails_count = 0
        for ch in range(i):
            str_to_add += chr(ch)
        bf_jenkins.add(str_to_add)
        if not bf_jenkins.check(str_to_add):
            fails_count += 1
    assert fails_count < 60, 'fails_count does not converge to 50'


def test_raises_error_when_unrecognized_hash_passed():
    with pytest.raises(Exception):
        Bloom_filter(hashfunc='34')
