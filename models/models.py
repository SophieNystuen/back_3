import datetime
class Events:
    name: str
    event_time: datetime.datetime
    notification_offset: int
    notification_text: str
    trigger_time: datetime.datetime


class Schedule:
    events: [Events]

