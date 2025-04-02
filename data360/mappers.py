from data360.model import Asset, AssetClass, AssetType


def ifKeyExists(data: dict, key: str) -> int | bool | str | None:
    """
    Check if a key exists in a dictionary and return its value if it exists.
    :param key: The key to check.
    :param data: The dictionary to check.
    :return: The value of the key if it exists, otherwise None.
    """
    return data[key] if key in data else None


def map_to_asset_class(data: dict) -> AssetClass:
    """
    Map the API response to an AssetClass object.
    :param data: The API response data.
    :return: An AssetClass object.
    """
    return AssetClass(
        id=data["ID"],
        value=data["Value"],
        name=data["Name"],
        description=data["Description"],
        allow_comments_on_asset=data["AllowCommentsOnAsset"],
    )


def map_to_asset_type(data: dict) -> AssetType:
    """
    Map the API response to an AssetType object.
    :param data: The API response data.
    :return: An AssetType object.
    """
    return AssetType(
        uid=data["uid"],
        name=data["Name"],
        asset_class=map_to_asset_class(data["Class"]),
        description=data["Description"],
        auto_display_description=data["AutoDisplayDescription"],
        hierarchical=data["Hierarchical"],
        hierarchy_maximum_depth=data["HierarchyMaximumDepth"],
        display_format=data["DisplayFormat"],
        notes=data["Notes"],
        use_as_transformation=data["UseAsTransformation"],
        can_own_fusion=data["CanOwnFusion"],
        path=data["Path"],
        icon_style=data["IconStyle"] if "IconStyle" in data else None,
        auto_display_parent=data["AutoDisplayParent"]
        if "AutoDisplayParent" in data
        else None,
        can_edit_parent=data["CanEditParent"],
        is_description_enabled=data["IsDescriptionEnabled"],
        is_description_visible_by_default=data["IsDescriptionVisibleByDefault"],
        is_default_read_access_enabled=data["IsDefaultReadAccessEnabled"],
        description_button_name=data["DescriptionButtonName"]
        if "DescriptionButtonName" in data
        else None,
    )


def map_to_asset(data: dict) -> Asset:
    return Asset(
        AssetId=data["AssetId"],
        AssetUid=data["AssetUid"],
        XrefId=data["XrefId"],
        AssetTypeUid=data["AssetTypeUid"],
        UpdatedOn=data["UpdatedOn"],
        CreatedOn=data["CreatedOn"],
        Color=data["Color"],
        Path=data["Path"],
        DisplayPath=data["DisplayPath"],
        Name=data["Name"],
        BusinessTerm=ifKeyExists(data, "BusinessTerm"),
        DataPoint=ifKeyExists(data, "DataPoint"),
        BusinessTermDefinition=ifKeyExists(data, "BusinessTermDefinition"),
        DataPointDefinition=ifKeyExists(data, "DataPointDefinition"),
        Key=ifKeyExists(data, "Key"),
        DataPrivacyType=ifKeyExists(data, "DataPrivacyType"),
        Integrity=ifKeyExists(data, "Integrity"),
        Confidentiality=ifKeyExists(data, "Confidentiality"),
        QltyScore=ifKeyExists(data, "QltyScore"),
        Critical=ifKeyExists(data, "Critical"),
        GovernanceScore=ifKeyExists(data, "GovernanceScore"),
        Suggestedcritical=ifKeyExists(data, "SuggestedCritical"),
        DataClassifiedBy=ifKeyExists(data, "DataClassifiedBy"),
    )
