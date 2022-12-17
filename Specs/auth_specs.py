from Helpers import *


# Login with valid data and assert that response has key "token"
def test_successful_login():
    response = login("admin", "password123")
    assert_ok_status_code(response)
    print('res', response.json())
    assert response.json()['token'] is not None


# Login with invalid credentials and assert on the returned error
def test_invalid_login():
    response = login("hamada", "password1233334d")
    assert_ok_status_code(response)
    assert response.json()['reason'] == 'Bad credentials'
