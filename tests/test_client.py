# import requests for the purposes of monkeypatching
import requests

from data360.client import Data360Instance as Data360Instance
from tests.conftest import MockResponse


def test_initialization():
    client = Data360Instance("https://example.com", "api_key", "api_secret")
    assert client.url == "https://example.com/api/v2"
    assert client.auth_key == "api_key" + ";" + "api_secret"


def test_requests_includes_authorization_header(monkeypatch):
    call_args = []

    # Mock the requests.get method
    def mock_get(url, headers=None, params=None):
        call_args.append(headers)
        call_args.append(params)
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    client = Data360Instance("https://example.com", "api_key", "api_secret")
    client.http_request("/test")

    # Check that the mock response is returned
    assert "Authorization" in call_args[0]
