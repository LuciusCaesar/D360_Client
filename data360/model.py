from dataclasses import dataclass
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


def to_camel(string: str) -> str:
    """
    Converts a string from snake_case to CamelCase (upper camel case aka PascalCase).
    """
    return "".join(word.capitalize() for word in string.split("_"))


class PascalCaseObject(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,  # Automatically generates the alias for attributes in CamelCase to comply with the API convention.  Used in serialization/deserialization into json.
        populate_by_name=True,  # Allows to use the class attribute name in the code instead of the alias
        frozen=True,  # Make all classes immutable (Functional programming rocks!)
    )


class AssetClass(PascalCaseObject):
    """
    Represents an Asset Class in the Data360 system.
    """

    id: int | str = Field(alias="ID")
    value: str
    name: str
    description: str
    allow_comments_on_asset: bool

    def __eq__(self, other):
        if not isinstance(other, AssetClass):
            return NotImplemented
        # Compare all fields except 'id'
        return (
            self.value == other.value
            and self.name == other.name
            and self.description == other.description
            and self.allow_comments_on_asset == other.allow_comments_on_asset
        )

    def __hash__(self):
        # Hash only the fields used in __eq__
        return hash(
            (
                self.value,
                self.name,
                self.description,
                self.allow_comments_on_asset,
            )
        )


# Assets
class AssetClassName(Enum):
    """
    Enum representing the names of asset classes in the Data360 system.
    """

    GENERIC = "Generic"
    BUSINESS_ASSET = "Business Asset"
    MODEL = "Model"
    POLICY = "Policy"
    RULE = "Rule"
    TECHNICAL_ASSET = "TechnicalAsset"
    REFERENCE = "Reference"
    USER = "User"
    GROUP = "Group"
    REFERENCE_ITEM_TYPE = "ReferenceItemType"
    DIAGRAM = "Diagram"
    METRIC_ALLOCATION = "MetricAllocation"
    PREDICATE = "Predicate"
    SEMANTIC_TYPE = "SemanticType"
    GLOSSARY = "Glossary"


class AssetType(PascalCaseObject):
    """
    Represents an asset type in the Data360 system.
    """

    id: int | None = Field(alias="ID", default=None)
    uid: str = Field(alias="uid")
    name: str
    asset_class: AssetClass = Field(alias="Class")
    description: str
    auto_display_description: bool | None = None
    hierarchical: bool | None = None
    hierarchy_maximum_depth: int | None = None
    display_format: str | None = None
    notes: str | None = None
    use_as_transformation: bool | None = None
    can_own_fusion: bool | None = None
    path: str | None = None
    can_edit_parent: bool | None = None
    is_description_enabled: bool | None = None
    is_description_visible_by_default: bool | None = None
    is_default_read_access_enabled: bool | None = None
    icon_style: dict | None = None
    flow_object_type: str | None = None
    auto_display_parent: bool | None = None
    description_button_name: str | None = None

    def __eq__(self, other):
        if not isinstance(other, AssetClass):
            return NotImplemented
        # Compare all fields except 'id'
        return self.name == other.name

    def __hash__(self):
        # Hash only the fields used in __eq__
        return hash((self.name,))


class Asset(PascalCaseObject):
    """
    Represents an asset in the Data360 system.
    """

    asset_id: int
    asset_uid: str
    xref_id: str | None = None
    asset_type_id: int
    asset_type_uid: str
    updated_on: str
    created_on: str
    color: str | None = None
    path: str
    display_path: str
    name: str
    business_term: str | None = None
    data_point: str | None = None
    business_term_definition: str | None = None
    data_point_definition: str | None = None
    key: str
    data_privacy_type: str | None = None
    integrity: str | None = None
    confidentiality: str | None = None
    qlty_score: str | None = None
    critical: str | None = None
    governance_score: str | None = None
    suggested_critical: str | None = None
    data_classified_by: str | None = None

    def __hash__(self):
        return hash(self.asset_uid)


# Relationships
class Cardinality(Enum):
    """
    Enum representing the cardinality of relationships in the Data360 system.
    """

    ONE = "One"
    MANY = "Many"


@dataclass(frozen=True)
class PredicateType:
    """
    Enum representing the names of predicate types in the Data360 system.
    """

    Type: str
    Name: str
    Description: str


@dataclass(frozen=True)
class Predicate:
    Uid: str
    Name: str
    Inverse: str
    Type: PredicateType
    IsSystem: bool
    IsInUse: bool


@dataclass(frozen=True)
class RelationshipType:
    """
    Represents a relationship type in the Data360 system.
    """

    Id: int
    Uid: str
    State: str
    IsSystem: bool
    Predicate: Predicate
    Subject: AssetType
    SubjectCardinality: Cardinality
    Object: AssetType
    ObjectCardinality: Cardinality


@dataclass(frozen=True)
class Relationship:
    """
    Represents a relationship in the Data360 system.
    """

    Uid: str
    RelationshipType: RelationshipType
    State: str
    Predicate: Predicate
    Subject: Asset
    Object: Asset


@dataclass(frozen=True)
class SearchFieldType:
    """
    Represents a search field type in the Data360 system.
    """

    AddToResult: bool
    Prefix: str
    Suffix: str
    DisplayOrder: int


@dataclass(frozen=True)
class DefinitionFieldType:
    """
    Represents a definition type in the Data360 system.
    """

    DisplayAsList: bool
    DisplayAssignmentSource: bool
    ExpandGroupMembership: bool
    ResponsibilityType: int
    ResponsibilityTypeUid: str


@dataclass(frozen=True)
class BooleanFieldType:
    """
    Represents a Boolean field type in the Data360 system.
    """

    DefaultValue: bool
    Description: dict
    Validation: dict
    Search: SearchFieldType
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class ComputedOwnershipLookupFieldType:
    """
    Represents a computed ownership lookup field type in the Data360 system.
    """

    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    Description: dict  # {"Display": "string"}
    Definition: DefinitionFieldType
    IsDisplayable: bool
    IsListable: bool
    ShowIfEmpty: bool
    HideFilter: bool
    HideFooter: bool
    HideHeader: bool
    DisplayInColumn: bool


@dataclass(frozen=True)
class ComputedRelationshipFieldType:
    """
    Represents a computed relationship field type in the Data360 system.
    """

    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    Description: dict
    IntersectTypeUid: str
    IntersectTypeName: str
    FieldTypeName: str
    IsDisplayable: bool
    IsListable: bool
    ShowIfEmpty: bool
    IsPrimaryFilter: bool
    Search: SearchFieldType
    DisplayInColumn: bool


@dataclass(frozen=True)
class ComputedRelationshipLookupFieldType:
    """
    Represents a computed relationship lookup field type in the Data360 system.
    """

    ColumnOrder: int
    Description: dict
    Definition: dict
    IsDisplayable: bool
    ShowIfEmpty: bool
    HideFilter: bool
    HideFooter: bool
    HideHeader: bool


@dataclass(frozen=True)
class ComputedRelationshipReferenceListFieldType:
    """
    Represents a computed relationship reference list field type in the Data360 system.
    """

    ColumnOrder: int
    Description: dict
    IntersectTypeUid: str
    IntersectTypeName: str
    IsDisplayable: bool
    ShowIfEmpty: bool
    DisplayRefListDescription: bool


@dataclass(frozen=True)
class ReferenceListFieldType:
    """
    Represents a reference list field type in the Data360 system.
    """

    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    Description: dict
    IsDisplayable: bool
    ShowIfEmpty: bool
    DisplayRefListDescription: bool
    DisplayRefListInTable: bool
    IsListable: bool


@dataclass(frozen=True)
class CounterFieldType:
    """
    Represents a counter field type in the Data360 system.
    """

    Description: dict
    Search: SearchFieldType
    CounterPrefix: str
    CounterInitialIndex: int
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class DateFieldType:
    """
    Represents a date field type in the Data360 system.
    """

    DefaultValue: str
    Description: dict
    Validation: dict
    Search: SearchFieldType
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class DateTimeFieldType:
    """
    Represents a date-time field type in the Data360 system.
    """

    DefaultValue: str
    Description: dict
    Validation: dict
    Search: SearchFieldType
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class DecimalFieldType:
    """
    Represents a decimal field type in the Data360 system.
    """

    DefaultValue: float
    Description: dict
    Increment: float
    Validation: dict
    Search: SearchFieldType
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class HtmlFieldType:
    """
    Represents an HTML field type in the Data360 system.
    """

    DefaultValue: str
    Description: dict
    Validation: dict
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class JsonFieldType:
    """
    Represents a JSON field type in the Data360 system.
    """

    ColumnOrder: int
    Description: dict
    Validation: dict
    IsDisplayable: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class JsonElementFieldType:
    """
    Represents a JSON element field type in the Data360 system.
    """

    JsonAttribute: dict
    Description: dict
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsListable: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class LinkFieldType:
    """
    Represents a link field type in the Data360 system.
    """

    DefaultValue: dict
    Description: dict
    Validation: dict
    Search: SearchFieldType
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class LookupFieldType:
    """
    Represents a lookup field type in the Data360 system.
    """

    DefaultValue: str
    DefaultFormattedValue: str
    Description: dict
    AllowAllValue: bool
    AllowAllLabel: str
    ParentFieldTypeName: str
    Filter: dict
    Format: dict
    List: dict
    Validation: dict
    Search: SearchFieldType
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class NumberFieldType:
    """
    Represents a number field type in the Data360 system.
    """

    DefaultValue: float
    Description: dict
    Increment: float
    Validation: dict
    Search: SearchFieldType
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class PathFieldType:
    """
    Represents a path field type in the Data360 system.
    """

    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    Description: dict
    IsDisplayable: bool
    IsListable: bool
    DisplayInColumn: bool
    Definition: dict


@dataclass(frozen=True)
class RelationshipFieldType:
    """
    Represents a relationship field type in the Data360 system.
    """

    Description: dict
    IntersectTypeUid: str
    IntersectTypeName: str
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    ShowIfEmpty: bool
    IsPrimaryFilter: bool
    DisplayInColumn: bool
    Search: SearchFieldType
    UseDisplayFormat: bool
    IsSubject: bool


@dataclass(frozen=True)
class TextFieldType:
    """
    Represents a text field type in the Data360 system.
    """

    DefaultValue: str
    Description: dict
    Validation: dict
    Search: SearchFieldType
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class TagFieldType:
    """
    Represents a tag field type in the Data360 system.
    """

    ColumnOrder: int
    ColumnWidth: int
    Description: dict
    SortOrder: int
    SortByAscending: bool
    IsListable: bool
    IsPrimaryFilter: bool
    TagTypeUID: str
    TagTypeID: int


@dataclass(frozen=True)
class ScoreFieldType:
    """
    Represents a score field type in the Data360 system.
    """

    ScoreType: str
    IsDisplayable: bool
    IsListable: bool
    ShowIfEmpty: bool
    IsPrimaryFilter: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    Description: dict
    DisplayInColumn: bool


@dataclass(frozen=True)
class SystemFieldType:
    """
    Represents a system field type in the Data360 system.
    """

    DefaultValue: str
    Description: dict
    Validation: dict
    Search: SearchFieldType
    DisplayInColumn: bool
    ColumnOrder: int
    ColumnWidth: int
    SortOrder: int
    SortByAscending: bool
    IsDisplayable: bool
    IsEditable: bool
    IsListable: bool
    IsPartOfKey: bool
    IsPrimaryFilter: bool
    ShowIfEmpty: bool


@dataclass(frozen=True)
class FieldAsset:
    """
    Represents a field in the Data360 system.
    """

    Name: str
    FriendlyName: str
    Category: str
    ActionTypeUid: str
    AssetTypeUid: str
    RelationshipTypeUid: str
    Id: int
    Type: (
        SearchFieldType
        | BooleanFieldType
        | ComputedOwnershipLookupFieldType
        | ComputedRelationshipFieldType
        | ComputedRelationshipLookupFieldType
        | ComputedRelationshipReferenceListFieldType
        | ReferenceListFieldType
        | CounterFieldType
        | DateFieldType
        | DateTimeFieldType
        | DecimalFieldType
        | HtmlFieldType
        | JsonFieldType
        | JsonElementFieldType
        | LinkFieldType
        | LookupFieldType
        | NumberFieldType
        | PathFieldType
        | RelationshipFieldType
        | TextFieldType
        | TagFieldType
        | ScoreFieldType
        | SystemFieldType
    )
