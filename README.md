## Flask, Event Streams, and Hotwire/Turbo

I was curious, so I got it to "work".

### Try it

You'll need Redis running at `redis://localhost:6379`. If it's somewhere else,
update the URL in sse.py.

1. `pip install -r requirements.txt`
1. `gunicorn sse:app --worker-class gevent --bind 127.0.0.1:8000`
    * `--log-level debug` is optional, but useful

Connect a couple browser tabs to http://127.0.0.0.1:8000. Open another one to
http://127.0.0.1/randomness and watch.

There's also a `/chat` route that takes a `?body=` param if you want to chat
with yourself.
