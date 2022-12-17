
def assert_on_status_code(code, response):
    assert response.status_code == code


def assert_ok_status_code(response):
    assert_on_status_code(200, response)


def assert_created_status_code(response):
    assert_on_status_code(201, response)


def assert_no_content_status_code(response):
    assert_on_status_code(204, response)


def assert_bad_request_status_code(response):
    assert_on_status_code(400, response)


def assert_unauthorized_status_code(response):
    assert_on_status_code(401, response)


def assert_forbidden_status_code(response):
    assert_on_status_code(403, response)


def assert_notfound_status_code(response):
    assert_on_status_code(404, response)
