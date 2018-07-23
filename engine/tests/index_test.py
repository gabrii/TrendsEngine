from collections import Counter

import pytest

from backends import MemoryBackend
from date_tools import from_timestamp, date
from index import Index


@pytest.fixture()
def epoch() -> date:
    return from_timestamp(0)


@pytest.fixture()
def i() -> Index:
    b = MemoryBackend()  # We are using the o memory backend as a "mock"
    i = Index(b)
    return i


@pytest.mark.parametrize("text, expected_counter", [
    ("A", Counter(A=1)),
    ("A B", Counter(A=1, A_B=1, B=1)),
    ("A B C", Counter(A=1, A_B=1, B=1, B_C=1, C=1)),
])
def test_word_combinations(text, expected_counter: Counter, i: Index, epoch: date):
    """Add date suffix"""
    EPOCH_SUFFIX: str = ":1970:1"
    expected_counter_dated = Counter(**{key + EPOCH_SUFFIX: value for key, value in expected_counter.items()})

    i.index_text(text, epoch)
    assert i.backend.counter == expected_counter_dated
