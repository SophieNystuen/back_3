from flask import Flask
app = Flask(__name__)

@app.route('/schedule', methods = ['GET'])
def get_schedule():
   return 'Hello GET'

@app.route('/schedule', methods = ['POST'])
def post_schedule():
   return 'Hello POST'

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()