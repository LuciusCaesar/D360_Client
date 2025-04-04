import requests

# from data360.mappers import map_to_asset, map_to_asset_class, map_to_asset_type
from data360.loose_model import Asset, AssetClass, AssetType, Field
from data360.model import AssetClassName


class Data360Instance:
    def __init__(self, url: str, api_key: str, api_secret: str):
        """
        Initialize a Data360 instance with the given URL and API key.
        :param url: The base URL of the Data360 instance.
        :param api_key: The API key for authentication.
        """
        self.auth_key = api_key + ";" + api_secret
        self.url = url + "/api/v2"

    def http_request(
        self, method_url: str, headers: dict = {}, params={}
    ) -> requests.Response:
        """
        Make a GET request to the Data360 API.
        :param method_url: The URL of the API method.
        :param headers: The headers for the request.
        :param params: The parameters for the request.
        :return: The response from the API.
        """
        headers["Authorization"] = self.auth_key
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        response = requests.get(self.url + method_url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch data: {response.status_code} - {response.text}"
            )
        else:
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
        # asset_classes = [map_to_asset_class(item) for item in response.json()]
        asset_classes = [AssetClass(**item) for item in response.json()]
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
        # asset_types = [map_to_asset_type(item) for item in response.json()]
        asset_types = [AssetType(**item) for item in response.json()]
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
        # assets = [map_to_asset(item) for item in response.json()["items"]]
        assets = [Asset(**item) for item in response.json()["items"]]
        return assets

    def get_fields_by_asset_type(self, asset_type: AssetType) -> list[Field]:
        """
        Get the fields for a specific asset type from the Data360 instance.
        :param data360_instance: The Data360 instance.
        :param asset_type: The asset type to get fields for.
        :return: A list of Field objects.
        """
        return self.get_firlds_by_asset_type_uid(asset_type.uid)

    def get_fields_by_asset_type_uid(self, asset_type_uid: str) -> list[Field]:
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
        # fields = [map_to_asset(item) for item in response.json()["items"]]
        fields = [Field(**item) for item in response.json()["items"]]
        return fields
