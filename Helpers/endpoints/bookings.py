import json
import requests

from Constants import *


def get_all_bookings():
    response = requests.get(
        booking_url,
        headers={
            'Content-Type': 'application/json',
        }
    )
    return response


def get_bookings_by_name(firstname, lastname):
    response = requests.get(
        f' {booking_url}?firstname={firstname}&lastname={lastname}',
        headers={
            'Content-Type': 'application/json',
        }
    )
    return response


def get_flight_details_by_id(flight_id):
    response = requests.get(
        f'{booking_url}/{flight_id}',
        headers={
            'Content-Type': 'application/json',
        }
    )
    return response


def create_booking(booking_sample):
    response = requests.post(
        booking_url,
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        data=json.dumps(booking_sample)
    )
    return response
