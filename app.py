from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/health', methods=['GET'])
def health():
    return "Healthy: OK"

if __name__ == '__main__':
    app.run()
