import requests
from time import sleep
from datetime import datetime


#     response = requests.get('http://127.0.0.1:5000/history')
#     data = response.json()
#     for message in data['messages']:
#         print(message)
# 
#     sleep(1)

last_message_time = 0

while True:

    response = requests.get(
        'http://127.0.0.1:5000/history',
        params = {'after': last_message_time}
    )
    data = response.json()
    for message in data['messages']:
        print(datetime.fromtimestamp(message['time']).strftime('%H:%m:%S'),
                message['username'])
        print(message['text'])
        print()
        last_message_time = message['time']

    sleep(1)
