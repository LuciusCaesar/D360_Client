from dataclasses import dataclass
from enum import Enum


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


@dataclass(frozen=True)
class AssetClass:
    """
    Represents an asset class in the Data360 system.
    """

    ID: str
    Value: AssetClassName
    Name: AssetClassName
    Description: str
    AllowCommentsOnAsset: bool

    def __init__(self, **input):
        self.__dict__.update(input)


@dataclass(frozen=True)
class AssetType:
    """
    Represents an asset type in the Data360 system.
    """

    uid: str
    Name: str
    Class: AssetClass
    Description: str
    AutoDisplayDescription: bool
    Hierarchical: bool
    HierarchyMaximumDepth: int
    DisplayFormat: str
    Notes: str
    UseAsTransformation: bool
    CanOwnFusion: bool
    Path: str
    CanEditParent: bool
    IsDescriptionEnabled: bool
    IsDescriptionVisibleByDefault: bool
    IsDefaultReadAccessEnabled: bool
    IconStyle: dict | None
    FlowObjectType: str | None
    AutoDisplayParent: bool | None
    DescriptionButtonName: str | None

    def __init__(self, **input):
        self.__dict__.update(input)


@dataclass(frozen=True)
class Asset:
    """
    Represents an asset in the Data360 system.
    """

    AssetId: int
    AssetUid: str
    XrefId: str
    AssetTypeId: int
    AssetTypeUid: str
    UpdatedOn: str
    CreatedOn: str
    Color: str
    Path: str
    DisplayPath: str
    Name: str
    BusinessTerm: str | None
    DataPoint: str | None
    BusinessTermDefinition: str | None
    DataPointDefinition: str | None
    Key: str
    DataPrivacyType: str
    Integrity: str
    Confidentiality: str
    QltyScore: str | None
    Critical: str | None
    GovernanceScore: str | None
    Suggestedcritical: str | None
    DataClassifiedBy: str | None

    def __init__(self, **input):
        self.__dict__.update(input)


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
class DefinitionType:
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
    Definition: DefinitionType
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
class Field:
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
