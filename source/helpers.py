import time


def get_current_time() -> int:
    """Get current time in ms

    Returns:
        int: time in ms
    """
    return int(round(time.time() * 1000))


def elapsed_time_in_seconds(t) -> int:
    """Calculates diff in seconds from t to now

    Args:
        t (int): time

    Returns:
        int: elapsed time in seconds
    """
    return (int(round(time.time() * 1000)) - t)/1000

def elapsed_time_in_milliseconds(t) -> int:
    """Calculates diff in ms from t to now

    Args:
        t (int): time

    Returns:
        int: elapsed time in ms
    """
    return int(round(time.time() * 1000)) - t