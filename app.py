from flask import Flask, request
import mock_db.sample_data as sample_data
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World 1'

@app.route('/schedule', methods = ['GET'])
def create_schedule():
    schedule_id = request.form.get("id")
    data = sample_data.schedule[schedule_id]
    return data

@app.route('/create_schedule', methods = ['POST'])
def query_and_send_notification():
    return "Notification sent"

if __name__ == '__main__':
    print("HI")
    app.run()