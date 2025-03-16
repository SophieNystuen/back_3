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

    child = { 
    "child_id_1": { 
        "name" : "matt" 
        "age" : "10" 
        "sex" : "male" 
        "intrests" : "playing tennis"   
    }

}
child = { 
    "child_id_2": { 
        "name" : "kiara" 
        "age" : "6" 
        "sex" : "female" 
        "intrests" : ""   
    }

}

    FAQ = {
    "FAQ_id_1": { 
        "where is the 1st aid box?" : "cabinet in the 1st floor bathroom" 
        "where are the emergency contacts?" : "On the fridge"
        "what can the kid watch?" : " movie [netflix, disney]" 
        " can '' get a treat?" : "After they are done with their must do items[piano practice, math hw]" 
                 }

        }
    rules = { 
        "rules_id_1": {
            "rule 1" : "vegetarian diet only - no meat and no eggs"
            "rule 2" : "we tidy up after playtime. Put away toys and books after use." 
            "rule 3": "be kind to each other. No hitting, pushing, or hurting others."
            "rule 4": "use nice words. speak politely and respectfully to everyone in the house"
            "rule 5" : "screen time. no screens during meals and no screens after 8:00 P.M."
            "rule 6": "book time begins at 7:00 PM" 
            "rule 7": "tell a grownup if you need help or feel scared."
            }

        }


            
            
    
