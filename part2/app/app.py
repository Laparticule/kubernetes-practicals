# Hello World Counter App

from flask import Flask
import os, redis, time

app = Flask(__name__)
cache = redis.Redis(host=os.environ.get('REDIS_SERVICE'), port=6379)

def get_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def counter():
    return f"Hello, you've visited this page {get_count()} times!\n"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
