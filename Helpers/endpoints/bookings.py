from ..base_request import *
from Constants import *


def get_all_bookings():
    response = send_get_request(booking_url)
    return response


def get_bookings_by_name(firstname, lastname):
    response = send_get_request(f' {booking_url}?firstname={firstname}&lastname={lastname}')
    return response


def get_flight_details_by_id(flight_id):
    response = send_get_request(f'{booking_url}/{flight_id}')
    return response


def create_booking(booking_sample):
    response = send_post_request(booking_url, booking_sample)
    return response
