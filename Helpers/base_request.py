import requests
from pydash import py_
from Samples import *


def _generate_request_headers(token=None):
    if token is None:
        return get_sample('request-headers.json')
    else:
        return py_.set(
            py_.clone_deep(get_sample('request-headers.json')),
            'Authorization',
            token
        )


def send_get_request(url, token=None):
    if token is None:
        response = requests.get(url, headers=_generate_request_headers())
        return response
    else:
        response = requests.get(url, headers=_generate_request_headers(token))
        return response


def send_post_request(url, payload, token=None):
    if token is None:
        response = requests.post(url, headers=_generate_request_headers(), data=json.dumps(payload))
        return response
    else:
        response = requests.post(url, headers=_generate_request_headers(token), data=json.dumps(payload))
        return response


def send_put_request(url, payload, token=None):
    if token is None:
        response = requests.put(url, headers=_generate_request_headers(), data=json.dumps(payload))
        return response
    else:
        response = requests.put(url, headers=_generate_request_headers(token), data=json.dumps(payload))
        return response


def send_path_request(url, payload, token=None):
    if token is None:
        response = requests.patch(url, headers=_generate_request_headers(), data=json.dumps(payload))
        return response
    else:
        response = requests.patch(url, headers=_generate_request_headers(token), data=json.dumps(payload))
        return response


def send_delete_request(url, token=None):
    if token is None:
        response = requests.delete(url, headers=_generate_request_headers())
        return response
    else:
        response = requests.delete(url, headers=_generate_request_headers(token))
        return response

