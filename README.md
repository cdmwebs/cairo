## Flask, Event Streams, and Hotwire/Turbo

I was curious, so I got it to "work".

### How it Works

I had to spelunk in the Turbo source a bit, but basically you need an
`EventSource` to listen to an event-stream broadcasting from the
server.

Turbo needs to be have `connectStreamSource` called with the EventSource, then call `.start()`.

```javascript
const eventSource = new EventSource("/stream");
Turbo.connectStreamSource(eventSource);
Turbo.start();
```

When a [server-sent event comes across the wire][turbo] with a `message` type
and HTML in the body, Turbo looks for the `turbo-stream` template. If
found, it applies the `action` to the `target` element.

Here's my template for a message:

```jinja
<turbo-stream action="append" target="messages">
  <template>
    <div id="message_{{ id }}">Message is sent at {{ time }} seconds</div>
  </template>
</turbo-stream>
```

All the Flask stuff is demo code from the flask\_sse package.

### Try it

You'll need Redis running at `redis://localhost:6379`. If it's somewhere else,
update the URL in sse.py.

```
pip install -r requirements.txt
gunicorn sse:app --worker-class gevent --bind 127.0.0.1:8000
```

`--log-level debug` is optional, but useful

Connect a couple browser tabs to http://127.0.0.0.1:8000. Open another one to
http://127.0.0.1/randomness and watch.

There's also a `/chat` route that takes a `?body=` param if you want to chat
with yourself.

[turbo]: https://github.com/hotwired/turbo/blob/main/src/observers/stream_observer.ts#L69
