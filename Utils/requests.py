import requests


def post(url, headers, data):
    response = requests.post(url, headers, data)
    return response
