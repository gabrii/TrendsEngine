from collections import Counter

import pytest

from backends import MemoryBackend
from index import Index


@pytest.fixture()
def i():
    b = MemoryBackend()  # We are using the o memory backend as a "mock"
    i = Index(b)
    return i


@pytest.mark.parametrize("text, final_state", [
    ("hello", Counter(hello=1)),
    ("hello world", Counter(hello=1, hello_world=1, world=1)),
    ("hello world foo", Counter(hello=1, hello_world=1, world=1, world_foo=1, foo=1)),
])
def test_word_combinations(text, final_state: Counter, i: Index):
    i.index_text(text)
    assert i.backend.counter == final_state
