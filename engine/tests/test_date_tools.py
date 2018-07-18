from datetime import datetime

import pytest

from date_tools import from_timestamp, isocalendar


@pytest.fixture()
def epoch():
    return datetime(1970, 1, 1, 0, 0)  # Unix Epoch


def test_from_timestamp(epoch):
    x = from_timestamp(0)
    assert x == epoch


def test_week_isocalendar(epoch):
    w = isocalendar(epoch)
    assert w == (1970, 1, 4)


def test_right_now():
    now = datetime.utcnow()
    w = isocalendar(from_timestamp(now.timestamp()))

    assert w == now.isocalendar()
