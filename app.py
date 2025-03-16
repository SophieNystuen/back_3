from flask import Flask, request
import mock_db.sample_data as sample_data
import personal.secret as secret
import requests
import smtplib
app = Flask(__name__)

CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}

EMAIL = secret.EMAIL
PASSWORD = secret.GPASSWORD
PHONE_NUMBER = secret.PHONE
CARRIER = secret.CARRIER

@app.route('/')
def hello_world():
   return 'Hello World 1'

@app.route('/schedule', methods = ['GET'])
def create_schedule():
    schedule_id = request.form.get("id")
    data = sample_data.schedule[schedule_id]
    return data

@app.route('/send_notification', methods = ['POST'])
def query_and_send_notification():
    time = request.form.get("time")

    message = None

    events = sample_data.events

    for event_key in events:
        event = events[event_key]
        if event["time_to_trigger"] == time:
            message = event["trigger_message"]
    if message:
        recipient = PHONE_NUMBER + CARRIERS[CARRIER]
        auth = (EMAIL, PASSWORD)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(auth[0], auth[1])

        server.sendmail(auth[0], recipient, message)

        return "Notification sent"
    return "No message was sent, no trigger"

def get_events():
    return get_events()

def trigger_events():
    return


@app.route('/child', methods = ['GET'])
def get_child(): 
   child_id = request.form.get("id")
   data = sample_data.child[child_id]
    return data
   

if __name__ == '__main__':

    app.run()
