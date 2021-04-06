# Hello World App

from flask import Flask, abort
import socket, random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f"Hello, World! You've hit {socket.gethostname()}!\n"

@app.route('/health')
def health_check():
    if random.getrandbits(1):
        abort(500, "An error occured...")
    return f"App is healthy!\n"

@app.route('/text')
def text():
    text = ""
    with open("/usr/share/html/text.txt", "r") as f:
        text += f.read()
    return text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
