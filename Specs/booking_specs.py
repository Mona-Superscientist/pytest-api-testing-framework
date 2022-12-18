from Helpers import *


def test_get_all_flight_ids():
    response = get_all_bookings()
    assert_ok_status_code(response)
    assert len(response.json()) > 0
    for item in response.json():
        assert item['bookingid'] is not None

def 