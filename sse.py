import time
import random

from flask import Response, Flask, render_template, request
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost:6379"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/randomness')
def randomness():
    def sse_response():
        while True:
            send_time = str(time.time())
            template = render_template('message.html', id=random.randint(1, 10000), time=send_time)
            sse.publish(template, type='message')
            time.sleep(0.5)
            print('streamed', send_time)
    sse_response()
    return 'sending randomness every couple of seconds'


@app.route('/chat')
def publish_message():
    body = request.args.get('body', default = "nothing")
    template = render_template('message.html', id=random.randint(1, 10000), body=body)
    sse.publish(template, type='message')
    return template
