from datetime import datetime, date


def from_timestamp(timestamp: int) -> date:
    """Returns date from timestamp in utc."""
    return datetime.utcfromtimestamp(timestamp)


def isocalendar(_date: date) -> (int, int):
    """Wraper for isocaReturns a tuple with (year, week).
       The week is from ISO-8601 Calendar, not gregorian calendar weeks. This way each week has the same number of days."""
    year, week, day = _date.isocalendar()
    return year, week, day
