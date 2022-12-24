from jsonschema import validate
from Samples.samples_reader import load_json_schema


def assert_on_status_code(code, response):
    assert response.status_code == code


# ----------------- ASSERTIONS ON STATUS CODE ------------------
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


# ------------------ ASSERTIONS ON RESPONSE BODY -------------------
def check_response(response, key=None, value=None):
    assert response.json()[{key}] == value


def assert_on_expected_response(response, expected_response):
    assert response.json() == expected_response


# ---------------- ASSERTIONS ON JSON SCHEMA -----------------------
def assert_valid_schema(response, schema_file_name):
    schema = load_json_schema(schema_file_name)
    return validate(response.json(), schema)
