import json

from pydash import py_
from Helpers import *
from Samples import *
from Utils import *


def test_get_all_flight_ids():
    response = get_all_bookings()
    assert_ok_status_code(response)
    assert len(response.json()) > 0
    for item in response.json():
        assert item['booking'] is not None


def test_create_new_booking():
    firstname = generate_random_name()
    booking_sample = py_.clone_deep(get_sample('booking.json'))
    modified_sample = py_.set(booking_sample, 'firstname', firstname)
    response = create_booking(modified_sample)
    assert_ok_status_code(response)
    assert response.json()['bookingid'] is not None
    assert response.json()['booking']['firstname'] == firstname


