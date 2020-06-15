from flask import Flask, request
from datetime import datetime
import time
import random

app = Flask(__name__)
messages = [
    {'username': 'Jack', 'text': 'Hello!', 'time':  time.time()},
    {'username': 'Bonnie', 'text': 'HI', 'time': time.time()}

]

users = {
    #username:password
    'Jack': 'Amma1001',
    'Bonnie': '12345'

}

@app.route("/")
def hello():

    return {'hello': str(random.randint(0,2)), }

@app.route("/status")
def status():

    return {
        'status': True,
        'messages': len(messages),
        'users': len(users),
        'time': "copyright " + datetime.now().strftime('%h:%m')
        }

@app.route("/history")
def history():
    """
    request: -
    response:  {
        "message": [
            {'username': username, 'text':text, 'time':time.time()},
            ...
            ]
        }
    """

    after = float(request.args['after'])

    filtered_messages = [m for m in messages if after < m['time']]

    # filtered_messages = []
    # for message in messages:
    #     if after < message['time']:
    #         filtered_messages.append(message)

    return {'messages': filtered_messages}


@app.route("/send", methods = ['POST'])
def send():
    """
    request: {"username":"str", "text":"str"}
    response: {"ok": true}
    """
    data = request.json
    username = data['username']
    password = data['password']
    text = data['text']


    if username in users:
        real_password = users[username]
        if real_password != password:
            return {"ok": False}
    else:
        users[username] = password

    messages.append({'username': username, 'text':text, 'time':time.time()})

    return {"ok": True}

app.run()
