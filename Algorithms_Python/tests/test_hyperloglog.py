import pytest

from Algorithms_Python.hyperloglog import HyperLogLog


def test_can_create_hyperloglog():
    hll = HyperLogLog()
    assert isinstance(hll, HyperLogLog)


@pytest.mark.parametrize('precision, length',
                         [(14, 10),
                          (18, 50000)  # ,
                          # (25, 5000000)
                          ])
def test_cardinality(precision, length):
    hyperloglog = HyperLogLog(precision=precision)
    for i in range(length):
        hyperloglog.add(f"element{i}")
    estimated_cardinality = hyperloglog.count()
    assert estimated_cardinality < 1.01 * length
    assert estimated_cardinality > 0.99 * length
