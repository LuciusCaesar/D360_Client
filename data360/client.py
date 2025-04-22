import logging
from functools import cached_property

import requests

from data360.model import Asset, AssetClass, AssetClassName, AssetType, FieldAsset

logger = logging
logging.getLogger(__name__)
logging.basicConfig(filename="log.txt", encoding="utf-8", level=logging.DEBUG)


class Data360Instance:
    def __init__(self, url: str, api_key: str, api_secret: str):
        """
        Initialize a Data360 instance with the given URL and API key.
        :param url: The base URL of the Data360 instance.
        :param api_key: The API key for authentication.
        """
        self.auth_key = api_key + ";" + api_secret
        self.url = url + "/api/v2"

    @cached_property
    def asset_types(self) -> list[AssetType]:
        """Return the list of the asset types

        Returns:
            list[AssetType]: List of asset types
        """
        return self.get_asset_types()

    @cached_property
    def assets(self) -> list[Asset]:
        """Returns the list of Assets

        Returns:
            list[Asset]: List of assets
        """
        # need to filter USERS and GROUPS asset types as their kind of assets actually need another api method to work
        filtered_asset_types = [
            asset_type
            for asset_type in self.asset_types
            if asset_type.asset_class.name
            not in [AssetClassName.GROUP.value, AssetClassName.USER.value]
        ]
        assets = [
            asset
            for asset_type in filtered_asset_types
            for asset in self.get_asset_by_types(asset_type)
        ]
        return assets

    @cached_property
    def fields(self) -> list[FieldAsset]:
        fields_assets = [
            field
            for asset_type in self.asset_types
            for field in self.get_fields_by_asset_type(asset_type)
        ]
        return fields_assets

    def http_request(
        self, method_url: str, headers: dict | None = None, params: dict | None = None
    ) -> requests.Response:
        """
        Make a GET request to the Data360 API.
        :param method_url: The URL of the API method.
        :param headers: The headers for the request.
        :param params: The parameters for the request.
        :return: The response from the API.
        """
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        # Set default headers
        headers["Authorization"] = self.auth_key
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        logging.info(
            "Make HTTP Call",
        )
        response = requests.get(self.url + method_url, headers=headers, params=params)
        response.raise_for_status()
        return response

    def get_asset_class(self) -> list[AssetClass]:
        """
        Get the asset classes from the Data360 instance.
        :param data360_instance: The Data360 instance.
        :return: A list of AssetClass objects.
        """
        # Placeholder for actual API call
        method_url = "/assets/classes"
        response = self.http_request(method_url)
        json_response = response.json()
        asset_classes = [AssetClass.model_validate(json_response[0])]
        return asset_classes

    def get_asset_types(self, params={}) -> list[AssetType]:
        """
        Get the asset types from the Data360 instance.
        :param data360_instance: The Data360 instance.
        :return: A list of AssetType objects.
        """
        # Placeholder for actual API call
        method_url = "/assets/types"
        response = self.http_request(method_url, params=params)
        asset_types = [AssetType.model_validate(item) for item in response.json()]
        return asset_types

    def get_asset_types_by_class(self, asset_class: AssetClassName) -> list[AssetType]:
        """
        Get the asset types for a specific asset class from the Data360 instance.
        :param data360_instance: The Data360 instance.
        :param asset_class: The asset class to get asset types for.
        :return: A list of AssetType objects.
        """
        return self.get_asset_types({"Class": asset_class.value})

    def get_asset_by_types(self, asset_type: AssetType) -> list[Asset]:
        """
        Get the asset types from the Data360 instance.
        :param data360_instance: The Data360 instance.
        :return: A list of AssetType objects.
        """
        return self.get_asset_by_types_uid(asset_type.uid)

    def get_asset_by_types_uid(self, asset_type_uid: str) -> list[Asset]:
        """
        Get the asset types from the Data360 instance.
        :param data360_instance: The Data360 instance.
        :return: A list of AssetType objects.
        """
        # Placeholder for actual API call
        method_url = "/assets/" + asset_type_uid
        response = self.http_request(method_url)
        assets = [Asset.model_validate(item) for item in response.json()["items"]]
        return assets

    def get_fields_by_asset_type(self, asset_type: AssetType) -> list[FieldAsset]:
        """
        Get the fields for a specific asset type from the Data360 instance.
        :param data360_instance: The Data360 instance.
        :param asset_type: The asset type to get fields for.
        :return: A list of Field objects.
        """
        return self.get_fields_by_asset_type_uid(asset_type.uid)

    def get_fields_by_asset_type_uid(self, asset_type_uid: str) -> list[FieldAsset]:
        """
        Get the fields for a specific asset type from the Data360 instance.
        :param data360_instance: The Data360 instance.
        :param asset_type_uid: The asset type to get fields for.
        :return: A list of Field objects.
        """
        method_url = "/fields"
        response = self.http_request(
            method_url, params={"AssetTypeUid": asset_type_uid}
        )
        if "items" in response.json():
            fields = [
                FieldAsset.model_validate(item) for item in response.json()["items"]
            ]
        else:
            return []
        return fields
