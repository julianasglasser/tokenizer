import os
import sys

import requests
import pyperclip
import dotenv
from dotenv import load_dotenv


def get_auth_token(email, password):
    auth_payload = {
        'email': user_email,
        'password': user_password,
    }

    r = requests.post('%s/authenticate' % api_url,
                      json=auth_payload
                      ).json()
    return r.get('token', None)


def get_personify_token(auth_token, stonecode):
    if not auth_token:
        raise Exception('Authentication token not provided!\
            Verify your credentials.')

    personify_payload = {
        'stonecode': stonecode,
    }

    headers = {'Authorization': 'Bearer %s' % auth_token}
    r = requests.post('%s/v1/admin/personify' % api_url,
                      json=personify_payload,
                      headers=headers
                      ).json()
    token = r.get('token', None)

    if not token:
        raise Exception('Personify error! Verify value of STONECODE and \
            if you have the proper permission.')

    return token

if __name__ == '__main__':
    load_dotenv()
    user_email = os.getenv('USEREMAIL')
    user_password = os.getenv('USERPASSWORD')
    api_url = 'https://portalapi.stone.com.br'
    stonecode = sys.argv[1] if len(sys.argv) > 1 else os.getenv('STONECODE')

    print(user_email)
    print(user_password)
    print(stonecode)

    auth_token = get_auth_token(user_email, user_password)
    personify_token = get_personify_token(auth_token, stonecode)
    print('StoneCode: %s' % stonecode)
    print('Personified Token: %s' % personify_token)
    pyperclip.copy(str(personify_token))
    print('Personified Token copied to clipboard!')
