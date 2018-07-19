from collections import Counter

import pytest

from backends import MemoryBackend
from index import Index


@pytest.fixture()
def i():
    b = MemoryBackend()  # We are using the o memory backend as a "mock"
    i = Index(b)
    return i


@pytest.mark.parametrize("text, expected_counter", [
    ("A", Counter(A=1)),
    ("A B", Counter(A=1, A_B=1, B=1)),
    ("A B C", Counter(A=1, A_B=1, B=1, B_C=1, C=1)),
])
def test_word_combinations(text, expected_counter: Counter, i: Index):
    i.index_text(text)
    assert i.backend.counter == expected_counter
