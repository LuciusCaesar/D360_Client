import pytest
import requests

from data360.client import Data360Instance


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.fixture
def testing_d360(monkeypatch) -> None:
    """Mock the Data360 instance."""
    return Data360Instance(
        url="https://mock-url.com",
        api_key="mock_auth_key",
        api_secret="mock_auth_secret",
    )


# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:
    def __init__(self, json_response: str, status_code: int = 200):
        self.json_response = json_response
        self.status_code = status_code

    # mock json() method always returns a specific testing dictionary
    def json(self):
        return self.json_response


# monkeypatched requests.get moved to a fixture
def mock_response(monkeypatch, json_response) -> None:
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""

    def mock_get(*args, **kwargs):
        return MockResponse(json_response)

    monkeypatch.setattr(requests, "get", mock_get)


@pytest.fixture
def mock_get_asset_classes_response(monkeypatch) -> None:
    """Mock the response for get_asset_class."""
    json_response = [
        {
            "ID": 1,
            "Value": "BusinessAsset",
            "Name": "Business Asset",
            "Description": "Business assets.",
            "AllowCommentsOnAsset": True,
        },
        {
            "ID": 15,
            "Value": "Diagram",
            "Name": "Diagram",
            "Description": "Diagram asset.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 0,
            "Value": "Generic",
            "Name": "Generic Type",
            "Description": "Generic Type.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 12,
            "Value": "Group",
            "Name": "Group",
            "Description": "Group asset.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 16,
            "Value": "MetricAllocation",
            "Name": "MetricAllocation",
            "Description": "Metric Allocation.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 2,
            "Value": "Model",
            "Name": "Model",
            "Description": "Model assets.",
            "AllowCommentsOnAsset": True,
        },
        {
            "ID": 6,
            "Value": "Policy",
            "Name": "Policy",
            "Description": "Policy asset.",
            "AllowCommentsOnAsset": True,
        },
        {
            "ID": 17,
            "Value": "Predicate",
            "Name": "Predicate",
            "Description": "Predicate.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 9,
            "Value": "Reference",
            "Name": "Reference",
            "Description": "Reference asset.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 14,
            "Value": "ReferenceItemType",
            "Name": "Reference List",
            "Description": "Reference Item List.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 7,
            "Value": "Rule",
            "Name": "Rule",
            "Description": "Rule asset.",
            "AllowCommentsOnAsset": True,
        },
        {
            "ID": 18,
            "Value": "SemanticType",
            "Name": "SemanticType",
            "Description": "Semantic Type.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 8,
            "Value": "TechnicalAsset",
            "Name": "Technical Asset",
            "Description": "Technical asset that represent items like database columns, schemas, XML attributes, etc.",
            "AllowCommentsOnAsset": True,
        },
        {
            "ID": 11,
            "Value": "User",
            "Name": "User",
            "Description": "User asset.",
            "AllowCommentsOnAsset": True,
        },
    ]
    mock_response(monkeypatch, json_response)


@pytest.fixture
def mock_get_asset_types_response(monkeypatch) -> None:
    """Mock the response for get_asset_types."""
    json_response = [
        {
            "ID": 1,
            "Value": "BusinessAsset",
            "Name": "Business Asset",
            "Description": "Business assets.",
            "AllowCommentsOnAsset": True,
        },
        {
            "ID": 15,
            "Value": "Diagram",
            "Name": "Diagram",
            "Description": "Diagram asset.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 0,
            "Value": "Generic",
            "Name": "Generic Type",
            "Description": "Generic Type.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 12,
            "Value": "Group",
            "Name": "Group",
            "Description": "Group asset.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 16,
            "Value": "MetricAllocation",
            "Name": "MetricAllocation",
            "Description": "Metric Allocation.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 2,
            "Value": "Model",
            "Name": "Model",
            "Description": "Model assets.",
            "AllowCommentsOnAsset": True,
        },
        {
            "ID": 6,
            "Value": "Policy",
            "Name": "Policy",
            "Description": "Policy asset.",
            "AllowCommentsOnAsset": True,
        },
        {
            "ID": 17,
            "Value": "Predicate",
            "Name": "Predicate",
            "Description": "Predicate.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 9,
            "Value": "Reference",
            "Name": "Reference",
            "Description": "Reference asset.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 14,
            "Value": "ReferenceItemType",
            "Name": "Reference List",
            "Description": "Reference Item List.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 7,
            "Value": "Rule",
            "Name": "Rule",
            "Description": "Rule asset.",
            "AllowCommentsOnAsset": True,
        },
        {
            "ID": 18,
            "Value": "SemanticType",
            "Name": "SemanticType",
            "Description": "Semantic Type.",
            "AllowCommentsOnAsset": False,
        },
        {
            "ID": 8,
            "Value": "TechnicalAsset",
            "Name": "Technical Asset",
            "Description": "Technical asset that represent items like database columns, schemas, XML attributes, etc.",
            "AllowCommentsOnAsset": True,
        },
        {
            "ID": 11,
            "Value": "User",
            "Name": "User",
            "Description": "User asset.",
            "AllowCommentsOnAsset": True,
        },
    ]
    mock_response(monkeypatch, json_response)


@pytest.fixture
def mock_get_assets_response(monkeypatch) -> None:
    """Mock the response for get_asset_types."""
    json_response = {
        "items": [
            {
                "AssetId": 2917900,
                "AssetUid": "601c6864-d636-4b22-8f86-2dcde766a990",
                "XrefId": None,
                "AssetTypeId": 765,
                "AssetTypeUid": "50d59403-943a-4cec-b7e6-31f3145ba187",
                "UpdatedOn": "2025-02-06T16:25:44.717Z",
                "CreatedOn": "2025-02-06T16:25:44.717Z",
                "Color": None,
                "Path": "[APP-5].[Application]",
                "DisplayPath": "APP-5 / Application",
                "Name": "Application",
                "Description": "",
                "Acronyms": "",
                "Internal": None,
                "PortalWeblink": None,
                "Key": "APP-5",
            },
            {
                "AssetId": 2917926,
                "AssetUid": "bd4d98ac-7ab4-4ca3-ad0c-235dfd0908f2",
                "XrefId": None,
                "AssetTypeId": 765,
                "AssetTypeUid": "50d59403-943a-4cec-b7e6-31f3145ba187",
                "UpdatedOn": "2025-03-26T14:07:22.720Z",
                "CreatedOn": "2025-03-26T14:07:22.720Z",
                "Color": None,
                "Path": "[APP-6].[MIQ]",
                "DisplayPath": "APP-6 / MIQ",
                "Name": "MIQ",
                "Description": "<p>Application that aims at creating harmonized view on market data for the entire group. </p>",
                "Acronyms": "MIQ",
                "Internal": True,
                "PortalWeblink": None,
                "Key": "APP-6",
            },
        ],
        "pageSize": 200,
        "pageNum": 1,
        "total": 2,
    }
    mock_response(monkeypatch, json_response)


@pytest.fixture
def mock_get_fields_response(monkeypatch) -> None:
    """Mock the response for get_fields."""
    json_response = {
        "pageSize": 0,
        "pageNum": 0,
        "total": 0,
        "items": [
            {
                "Name": "string",
                "FriendlyName": "string",
                "Category": "string",
                "ActionTypeUid": "00000000-0000-0000-0000-000000000000",
                "AssetTypeUid": "00000000-0000-0000-0000-000000000000",
                "RelationshipTypeUid": "00000000-0000-0000-0000-000000000000",
                "Id": 0,
                "Type": {
                    "Boolean": {
                        "DefaultValue": True,
                        "Description": {"Form": "string", "Display": "string"},
                        "Validation": {"IsRequired": True},
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                    "ComputedOwnershipLookup": {
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "Description": {"Display": "string"},
                        "Definition": {
                            "DisplayAsList": True,
                            "DisplayAssignmentSource": True,
                            "ExpandGroupMembership": True,
                            "ResponsibilityType": 0,
                            "ResponsibilityTypeUid": "00000000-0000-0000-0000-000000000000",
                        },
                        "IsDisplayable": True,
                        "IsListable": True,
                        "ShowIfEmpty": True,
                        "HideFilter": True,
                        "HideFooter": True,
                        "HideHeader": True,
                        "DisplayInColumn": True,
                    },
                    "ComputedRelationshipField": {
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "Description": {"Display": "string"},
                        "IntersectTypeUid": "00000000-0000-0000-0000-000000000000",
                        "IntersectTypeName": "string",
                        "FieldTypeName": "string",
                        "IsDisplayable": True,
                        "IsListable": True,
                        "ShowIfEmpty": True,
                        "IsPrimaryFilter": True,
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "DisplayInColumn": True,
                    },
                    "ComputedRelationshipLookup": {
                        "ColumnOrder": 0,
                        "Description": {"Display": "string"},
                        "Definition": {
                            "Fields": [
                                {
                                    "AssetTypeUid": "00000000-0000-0000-0000-000000000000",
                                    "FieldTypeName": "string",
                                    "Filter": "string",
                                    "OverrideDisplayName": "string",
                                    "DisplayOrder": 0,
                                    "SortOrder": 0,
                                    "SortByAscending": True,
                                    "Show": True,
                                    "Width": 0,
                                    "RelationIndex": 0,
                                }
                            ],
                            "Relations": [
                                {
                                    "IntersectTypeUid": "00000000-0000-0000-0000-000000000000",
                                    "AssetTypeUid": "00000000-0000-0000-0000-000000000000",
                                    "RelationType": "StandardRelationship",
                                    "Direction": "Back",
                                }
                            ],
                            "Filters": "string",
                            "FiltersJSON": "string",
                        },
                        "IsDisplayable": True,
                        "ShowIfEmpty": True,
                        "HideFilter": True,
                        "HideFooter": True,
                        "HideHeader": True,
                    },
                    "ComputedRelationshipReferenceList": {
                        "ColumnOrder": 0,
                        "Description": {"Display": "string"},
                        "IntersectTypeUid": "00000000-0000-0000-0000-000000000000",
                        "IntersectTypeName": "string",
                        "IsDisplayable": True,
                        "ShowIfEmpty": True,
                        "DisplayRefListDescription": True,
                    },
                    "ReferenceList": {
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "Description": {"Display": "string"},
                        "IsDisplayable": True,
                        "ShowIfEmpty": True,
                        "DisplayRefListDescription": True,
                        "DisplayRefListInTable": True,
                        "IsListable": True,
                    },
                    "Counter": {
                        "Description": {"Form": "string", "Display": "string"},
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "CounterPrefix": "string",
                        "CounterInitialIndex": 0,
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                    "Date": {
                        "DefaultValue": "2025-04-07T08:16:30.611Z",
                        "Description": {"Form": "string", "Display": "string"},
                        "Validation": {"IsRequired": True},
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                    "DateTime": {
                        "DefaultValue": "2025-04-07T08:16:30.611Z",
                        "Description": {"Form": "string", "Display": "string"},
                        "Validation": {"IsRequired": True},
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                    "Decimal": {
                        "DefaultValue": 0,
                        "Description": {"Form": "string", "Display": "string"},
                        "Increment": 0,
                        "Validation": {
                            "Precision": 0,
                            "MinimumValue": 0,
                            "MaximumValue": 0,
                            "IsRequired": True,
                        },
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                    "Html": {
                        "DefaultValue": "string",
                        "Description": {"Form": "string", "Display": "string"},
                        "Validation": {
                            "MinimumLength": 0,
                            "MaximumLength": 0,
                            "IsRequired": True,
                        },
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                    "Json": {
                        "ColumnOrder": 0,
                        "Description": {"Display": "string"},
                        "Validation": {"IsRequired": True},
                        "IsDisplayable": True,
                        "ShowIfEmpty": True,
                    },
                    "JsonElement": {
                        "JsonAttribute": {
                            "FieldName": "string",
                            "Path": "string",
                            "DataType": "string",
                        },
                        "Description": {"Display": "string"},
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsListable": True,
                        "ShowIfEmpty": True,
                    },
                    "Link": {
                        "DefaultValue": {"Text": "string", "Url": "string"},
                        "Description": {"Form": "string", "Display": "string"},
                        "Validation": {"IsRequired": True},
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                    "Lookup": {
                        "DefaultValue": "string",
                        "DefaultFormattedValue": "string",
                        "Description": {"Form": "string", "Display": "string"},
                        "AllowAllValue": True,
                        "AllowAllLabel": "string",
                        "ParentFieldTypeName": "string",
                        "Filter": {
                            "FieldTypeName": "string",
                            "PredicateUid": "00000000-0000-0000-0000-000000000000",
                            "UseDirection": True,
                        },
                        "Format": {"Display": "string", "Edit": "string"},
                        "List": {
                            "Uid": "00000000-0000-0000-0000-000000000000",
                            "Class": "TechnicalAsset",
                            "AllowMultipleValues": True,
                            "TypeName": "string",
                        },
                        "Validation": {"IsRequired": True},
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                    "Number": {
                        "DefaultValue": 0,
                        "Description": {"Form": "string", "Display": "string"},
                        "Increment": 0,
                        "Validation": {
                            "MinimumValue": 0,
                            "MaximumValue": 0,
                            "IsRequired": True,
                        },
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                    "Path": {
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "Description": {"Display": "string"},
                        "IsDisplayable": True,
                        "IsListable": True,
                        "DisplayInColumn": True,
                        "Definition": {
                            "AssetTypeUid": "00000000-0000-0000-0000-000000000000",
                            "AssetTypeName": "string",
                        },
                    },
                    "Relationship": {
                        "Description": {"Form": "string", "Display": "string"},
                        "IntersectTypeUid": "00000000-0000-0000-0000-000000000000",
                        "IntersectTypeName": "string",
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "ShowIfEmpty": True,
                        "IsPrimaryFilter": True,
                        "DisplayInColumn": True,
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "UseDisplayFormat": True,
                        "IsSubject": True,
                    },
                    "Text": {
                        "DefaultValue": "string",
                        "Description": {"Form": "string", "Display": "string"},
                        "Validation": {
                            "Message": "string",
                            "Pattern": "string",
                            "MinimumLength": 0,
                            "MaximumLength": 0,
                            "IsRequired": True,
                        },
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                    "Tag": {
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "Description": {"Display": "string"},
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsListable": True,
                        "IsPrimaryFilter": True,
                        "TagTypeUID": "00000000-0000-0000-0000-000000000000",
                        "TagTypeID": 0,
                    },
                    "Score": {
                        "ScoreType": "Governance",
                        "IsDisplayable": True,
                        "IsListable": True,
                        "ShowIfEmpty": True,
                        "IsPrimaryFilter": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "Description": {"Display": "string"},
                        "DisplayInColumn": True,
                    },
                    "System": {
                        "DefaultValue": "string",
                        "Description": {"Form": "string", "Display": "string"},
                        "Validation": {
                            "Message": "string",
                            "Pattern": "string",
                            "MinimumLength": 0,
                            "MaximumLength": 0,
                            "IsRequired": True,
                        },
                        "Search": {
                            "AddToResult": True,
                            "Prefix": "string",
                            "Suffix": "string",
                            "DisplayOrder": 0,
                        },
                        "DisplayInColumn": True,
                        "ColumnOrder": 0,
                        "ColumnWidth": 0,
                        "SortOrder": 0,
                        "SortByAscending": True,
                        "IsDisplayable": True,
                        "IsEditable": True,
                        "IsListable": True,
                        "IsPartOfKey": True,
                        "IsPrimaryFilter": True,
                        "ShowIfEmpty": True,
                    },
                },
            }
        ],
    }
    mock_response(monkeypatch, json_response)
