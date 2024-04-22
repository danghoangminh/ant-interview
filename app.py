from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1><center>Hello World app! Version 1</center><h1>"

@app.route('/health')
def health_check():
    if all_required_services_are_running():
        return 'OK', 200
    else:
        return 'Service Unavailable', 500

def all_required_services_are_running():
    return True

def run_flask():
    app.run(host='0.0.0.0',port=8080)

if __name__ == '__main__':
    # Start the Flask app in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()