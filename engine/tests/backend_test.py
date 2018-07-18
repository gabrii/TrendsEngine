from collections import Counter

import pytest

from backends import MemoryBackend


@pytest.fixture()
def b():
    """Backend fixture"""
    return MemoryBackend()


def test_init(b):
    pass


def test_incr_default(b):
    b.incr('x')
    assert b.get('x') == 1


def test_incr_value(b):
    b.incr('x', 10)
    assert b.get('x') == 10


def test_unknown_key(b):
    assert b.get('x') == 0


def test_incr_many(b):
    b.incr_many(Counter({'x': 1, 'y': 10}))
    assert b.get('x') == 1
    assert b.get('y') == 10


def test_get_many(b):
    b.incr('x')
    b.incr('y', 10)
    many = b.get_many(['x', 'y'])
    assert many['x'] == 1
    assert many['y'] == 10


def test_incr_negative_value(b):
    b.incr('x', 5)
    b.incr('x', -10)
    b.incr('y', -10)
    assert b.get('x') == -5
    assert b.get('y') == -10
