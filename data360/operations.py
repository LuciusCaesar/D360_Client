import json

from data360 import client
from data360.meta_model import MetaModel, MetaModelDiff


def calculate_meta_model_difference(
    target: MetaModel,
    current: MetaModel,
) -> MetaModelDiff:
    """
    Calculate the difference between two meta models.
    """
    return MetaModelDiff(
        assets_to_be_added=list(set(target.asset) - set(current.asset)),
        assets_to_be_deleted=list(set(current.asset) - set(target.asset)),
    )


def update_attribute(attribute_name: str, new_uid: str, asset: object) -> object:
    """
    Update an attribute of an asset.
    """
    asset.__setattr__(attribute_name, new_uid)
    return asset


def update_attributes(
    attribute_name: str, new_uid: str, asset_list: list[object]
) -> list[object]:
    """
    Update and specific attribute for all assets in a list.
    """
    return [update_attribute(attribute_name, new_uid, asset) for asset in asset_list]


def migrate_fields(
    origin_env: client,
    destination_env: client,
    origin_asset_uid: str,
    destination_asset_uid: str,
):
    """
    Migrate fields from one environment to another.
    """
    origin_fields = origin_env.get_fields_by_asset_type_uid(origin_asset_uid)

    # Update the UIDs of the fields in the destination environment
    updated_destination_fields = update_attributes(
        "AssetTypeUid", destination_asset_uid, origin_fields
    )

    payload = json.dumps(
        [item.__dict__ for item in updated_destination_fields], indent=4
    )

    # Call the api
    response = destination_env.http_request("/fields", method="POST", data=payload)

    return response
