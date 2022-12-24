import pytest
from Helpers.endpoints.auth import login
from Helpers.endpoints.bookings import create_booking


@pytest.fixture()
def generate_auth_token():
    def _generate_auth_token(username, password):
        response = login(username, password)
        json_response = response.json()
        return json_response['token']

    return _generate_auth_token


@pytest.fixture()
def get_booking_id():
    def _get_booking_id(booking_sample):
        response = create_booking(booking_sample)
        json_response = response.json()
        return json_response['bookingid']

    return _get_booking_id
