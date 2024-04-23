import os
import platform
import psutil
import psycopg2
from flask import request
from flask import Flask
from threading import Thread
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry.instrumentation.wsgi import OpenTelemetryMiddleware
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor

# Configure Azure monitor collection telemetry pipeline
configure_azure_monitor()

# Get the database name, username, and password from environment variables
dbname = os.environ.get("POSTGRES_DB")
username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")

app = Flask(__name__)
app.wsgi_app = OpenTelemetryMiddleware(app.wsgi_app)
Psycopg2Instrumentor().instrument()

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

@app.before_request
def log_request_info():
    # Set up a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=dbname,
        user=username,
        password=password,
        host="postgres",
        port="5432"
    )

    # Create a cursor object
    cur = conn.cursor()

    # SQL query to insert data into the database
    query = """
    INSERT INTO logs (path, method, ip, time)
    VALUES (%s, %s, %s, NOW())
    """

    cur.execute(query, (request.path, request.method, request.remote_addr))
    conn.commit()
    cur.close()

@app.route('/health')
def health_check():
    if pgsql_check():
        return 'OK', 200
    else:
        return 'Service Unavailable', 500

def pgsql_check():
    try:
        # Test the PostgreSQL connection
        conn = psycopg2.connect(
            dbname=dbname,
            user=username,
            password=password,
            host="postgres",
            port="5432"
        )
        conn.close()
        return True
    except psycopg2.OperationalError:
        return False

def run_flask():
    app.run(host='0.0.0.0',port=8080)

if __name__ == '__main__':
    # Start the Flask app in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()