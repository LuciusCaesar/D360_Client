# import requests for the purposes of monkeypatching
import requests

from data360.client import Data360Instance as d360
from data360.model import Asset, AssetClass, AssetClassName, AssetType, FieldAsset
from tests.conftest import MockResponse
from tests.model_factory import AssetTypeFactory


def test_initialization():
    client = d360("https://example.com", "api_key", "api_secret")
    assert client.url == "https://example.com/api/v2"
    assert client.auth_key == "api_key" + ";" + "api_secret"


def test_requests_includes_authorization_header(monkeypatch):
    call_args = []

    # Mock the requests.get method
    def mock_get(url, headers=None, params=None):
        call_args.append(headers)
        call_args.append(params)
        return MockResponse(json_response={"mock_key": "mock_response"})

    monkeypatch.setattr(requests, "get", mock_get)

    client = d360("https://example.com", "api_key", "api_secret")
    client.http_request("/test")

    # Check that the mock response is returned
    assert "Authorization" in call_args[0]


def test_get_asset_class_parsing(testing_d360, mock_get_asset_classes_response):
    asset_classes = testing_d360.get_asset_class()

    # Assert all elements of the list are of type AssetClass
    assert len(asset_classes) >= 1
    assert all(isinstance(asset_class, AssetClass) for asset_class in asset_classes)


def test_get_asset_types(testing_d360, mock_get_asset_types_response):
    # Mock the requests.get method
    asset_types = testing_d360.get_asset_types()

    # Assert all elements of the list are of type AssetClass
    assert len(asset_types) >= 1
    assert all(isinstance(asset_class, AssetType) for asset_class in asset_types)


def test_get_asset_types_by_class(testing_d360, mock_get_asset_types_response):
    asset_types = testing_d360.get_asset_types_by_class(
        asset_class=AssetClassName.BUSINESS_ASSET
    )

    assert len(asset_types) >= 1
    assert all(isinstance(asset_class, AssetType) for asset_class in asset_types)


def test_get_asset_by_types(testing_d360, mock_get_assets_response):
    asset_type = AssetTypeFactory.build()

    assets = testing_d360.get_asset_by_types(asset_type)

    assert len(assets) >= 1
    assert all(isinstance(asset, Asset) for asset in assets)


def test_get_fields_by_asset_types(testing_d360, mock_get_fields_response):
    asset_type = AssetTypeFactory.build()

    fields = testing_d360.get_fields_by_asset_type(asset_type)

    assert len(fields) >= 1
    assert all(isinstance(field, FieldAsset) for field in fields)
