import requests

print('Enter your name:')
username = input()
print('Enter your password:')
password = input()

while True:
    print('Enter messages:')
    text = input()
    response = requests.post('http://127.0.0.1:5000/send',
                            json={'username':username, 'password':password, 'text':text }
                            )

    if not response.json()['ok']:
        print('access denied!')
        break
