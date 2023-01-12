from datetime import datetime


def to_datetime(dt: datetime):
    isoformat = datetime.fromisoformat(dt)
    return str(isoformat)


def custom_print(content):
    print("=" * 50)
    print(content)
    print("=" * 50)
