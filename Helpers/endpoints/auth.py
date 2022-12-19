from ..base_request import *
from Constants import routes


def login(username, password):
    payload = {
        'username': username,
        'password': password
    }
    response = send_post_request(routes.auth_url, payload)
    return response


def generate_auth_token(username, password):
    response = login(username, password)
    json_response = response.json()
    return json_response['token']

