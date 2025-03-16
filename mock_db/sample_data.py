class Event:
    name: str
    time: str

    def __init__(self, name, time):
        self


test_event = Event(name="name here", time="7.pm")

events = {
    "event_id_1": {
        "name": "Bed Time",
        "time": "9 p.m"
    }

}

schedule = {
    "schedule_id_1": {
        "events": [
            events["event_id_1"]
        ]
    }
}