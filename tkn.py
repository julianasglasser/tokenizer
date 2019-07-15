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

    try:
        r = requests.post('%s/authenticate' % api_url,
                          json=auth_payload
                          ).json()
        return r.get('token', None)
    except Exception as er:
        print('Something went wrong while trying to authenticate: ', er)
    return None

def get_personify_token(auth_token, stonecode):
    if not auth_token:
        raise Exception('Authentication token not provided! '\
            'Verify your credentials.')

    personify_payload = {
        'stonecode': stonecode,
    }

    headers = {'Authorization': 'Bearer %s' % auth_token}
    try:
        r = requests.post('%s/v1/admin/personify' % api_url,
                          json=personify_payload,
                          headers=headers
                          ).json()
        token = r.get('token', None)
    except Exception as er:
        print('Something went wrong while trying to personify: ', er)

    if not token:
        raise Exception('Personify error! Verify value of STONECODE and ' \
            'if you have the proper permission.')

    return token

if __name__ == '__main__':
    # TODO: check why it is not loading .env
    load_dotenv()
    user_email = os.getenv('USER_EMAIL')
    environ = 'prd' 
    if len(sys.argv) > 2 and len(sys.argv[2]) == 3:
        environ = sys.argv[2]
    elif len(sys.argv) > 1 and len(sys.argv[1]) == 3:
        environ = sys.argv[1]
    user_password = os.getenv('USER_{}_PASSWORD'.format(environ.upper()))
    api_url = os.getenv('API_{}_URL'.format(environ.upper()))
    stonecode = sys.argv[1] if len(sys.argv) > 1 and len(sys.argv[1]) == 9 else os.getenv('STONECODE')

    auth_token = get_auth_token(user_email, user_password)
    personify_token = get_personify_token(auth_token, stonecode)
    print('StoneCode: %s' % stonecode)
    print('Personified Token: %s' % personify_token)
    pyperclip.copy(str(personify_token))
    print('Personified Token copied to clipboard!')