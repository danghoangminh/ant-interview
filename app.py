import os
import platform
import psutil
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/v1')
def hello_world():
    return "<h1><center>Hello World app! Version 1</center><h1>"

@app.route('/')
def display_os_information():
    os_info = {
        "os_name": os.name,
        "platform": platform.system(),
        "platform_release": platform.release(),
        "cpu_usage": psutil.cpu_percent(interval=None),
        "ram_usage": psutil.virtual_memory().percent,
    }
    return os_info

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