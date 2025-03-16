events = {
    "event_id_1": {
        "name": "Bed Time",
        "time": "19:30",
        "trigger": "30",
        "time_to_trigger": "20:00",
        "trigger_message": "Start Beckett's bedtime routine(Bath, Stories, Brushing Teeth)",
    },
    "event_id_2": {
        "name": "Wake Up Beckett",
        "time": "07:00",
        "trigger": None,
        "time_to_trigger": None,
        "trigger_message": None,
    },
    "event_id_3" : {
        "name": "Breakfast",
        "time": "08:30",
        "trigger": 15,
        "time_to_trigger": "08:15",
        "trigger_message": "Start preparing Beckett's breakfast",
    },
    "event_id_4": {
        "name": "Lunch",
        "time": "12:30",
        "trigger": 15,
        "time_to_trigger": "12:15",
        "trigger_message": "Start preparing Beckett's Lunch",
    },
    "event_id_5": {
        "name": "Nap Time",
        "time": "14:30",
        "trigger": 15,
        "time_to_trigger": "14:15",
        "trigger_message": "Start preparing Beckett's Lunch",
    },
    "event_id_6": {
        "name": "Dinner Time",
        "time": "18:30",
        "trigger": 15,
        "time_to_trigger": "18:15",
        "trigger_message": "Start preparing Beckett's Dinner",
    }
}

schedule = {
    "schedule_id_1": {
        "events": [
            events["event_id_1"],
            events["event_id_2"],
            events["event_id_3"],
            events["event_id_4"],
            events["event_id_5"],
            events["event_id_6"],
        ]
    }
}