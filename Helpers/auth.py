import json
import requests

from Constants import routes


def login(username, password):
    payload = json.dumps({
        'username': username,
        'password': password
    })

    response = requests.post(
        routes.auth_url,
        headers={
            'Content-Type': 'application/json'
        },
        data=payload
    )

    return response


def generate_auth_token(username, password):
    response = login(username, password)
    json_response = response.json()
    return json_response['token']

