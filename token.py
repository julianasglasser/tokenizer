import os
import sys

import requests

import pyperclip

user_email = os.environ.get('USEREMAIL')
user_password = os.environ.get('USERPASSWORD')
api_url = 'https://portalapi.stone.com.br'
stonecode = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('STONECODE')
auth_payload = {
    'email': user_email,
    'password': user_password,
}
personify_payload = {
    'stonecode': stonecode,
}


def get_auth_token():
    return requests.post('%s/authenticate' % api_url,
                         json=auth_payload
                        ).json()['token']


def get_personify_token(auth_token):
    headers = {'Authorization': 'Bearer %s' % auth_token}
    return requests.post('%s/v1/admin/personify' % api_url,
                         json=personify_payload,
                         headers=headers
                        ).json()['token']


auth_token = get_auth_token()
personify_token = get_personify_token(auth_token)
print('StoneCode: %s' % stonecode)
print('Personified Token: %s' % personify_token)
pyperclip.copy(str(personify_token))
print('Personified Token copied to clipboard!')
