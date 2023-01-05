def string_to_day_minute(time: str) -> int:
    [hour, minute] = [int(value) for value in time.split(':')]

    if hour > 23 or minute > 59:
        raise ValueError("Value must be a time format between 00:00 and 23:59")

    return (hour * 60) + minute
