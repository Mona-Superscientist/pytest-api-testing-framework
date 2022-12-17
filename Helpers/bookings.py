import json
import requests

from Constants import routes


def get_all_bookings():
    response = requests.get(
        routes.booking_url,
        headers={
            'Content-Type': 'application/json',
        }
    )
    return response


def get_bookings_by_name(firstname, lastname):
    response = requests.get(
        f' {routes.booking_url}?firstname={firstname}&lastname={lastname}',
        headers={
            'Content-Type': 'application/json',
        }
    )
    return response


def get_flight_details_by_id(flight_id):
    response = requests.get(
        f'{routes.booking_url}/{flight_id}',
        headers={
            'Content-Type': 'application/json',
        }
    )
    return response


