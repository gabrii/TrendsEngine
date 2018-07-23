from datetime import datetime

import pytest

from date_tools import from_timestamp, isocalendar, date_suffix


@pytest.fixture(scope="module")
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
    w = isocalendar(from_timestamp(int(now.timestamp())))

    assert w == now.isocalendar()


def test_date_suffix(epoch):
    assert "1970:1" == date_suffix(epoch)
