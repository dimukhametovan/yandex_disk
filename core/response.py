import logging
import allure
from allure_commons.types import AttachmentType

logger = logging.getLogger(__name__)


class Response:

    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code

        logger.info(
            "HTTP %s %s -> %s",
            response.request.method,
            response.request.url,
            self.status_code,
        )

        try:
            body = response.text
        except Exception:
            body = "<unreadable body>"

        logger.debug("Response body: %s", body)

        self._attach_to_allure(body)

    def _attach_to_allure(self, body: str):
        allure.attach(
            body,
            name=f"Response {self.status_code}",
            attachment_type=AttachmentType.JSON,
        )

    def _is_json(self):
        ctype = self.response.headers.get("Content-Type", "")
        return "json" in ctype

    def json(self):
        return self.response.json()

    def assert_status(self, expected_status):
        assert self.status_code == expected_status, \
            f"Expected {expected_status}, got {self.status_code}"

    def assert_status_in(self, expected_statuses):
        assert self.status_code in expected_statuses, \
            f"Expected one of {expected_statuses}, got {self.status_code}"

    def assert_field(self, field, expected_value):
        actual_value = self.json().get(field)
        assert actual_value == expected_value, \
            f"{field}: expected {expected_value}, got {actual_value}"

    def assert_has_fields(self, *fields):
        body = self.json()
        missing = [f for f in fields if f not in body]
        assert not missing, f"Missing fields in response: {missing}"

    def assert_field_type(self, field, expected_type):
        body = self.json()
        assert field in body, f"Field {field} is missing"
        assert isinstance(body[field], expected_type), \
            f"{field}: expected type {expected_type}, got {type(body[field])}"
        
    def assert_field_contains(self, field, expected_substring: str):
        body = self.json()
        assert field in body, f"Field {field} is missing"
        value = str(body[field])
        assert expected_substring in value, \
            f"{field}: expected '{expected_substring}' in {value!r}"

    def assert_error(self, error_code: str):
        body = self.json()
        actual = body.get("error")
        assert actual == error_code, \
            f"error: expected {error_code}, got {actual}"
