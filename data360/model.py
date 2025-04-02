from dataclasses import dataclass
from enum import Enum


# Assets
class AssetClassName(Enum):
    """
    Enum representing the names of asset classes in the Data360 system.
    """

    GENERIC = "Generic"
    BUSINESS_ASSET = "BusinessAsset"
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

    id: str
    value: AssetClassName
    name: AssetClassName
    description: str
    allow_comments_on_asset: bool


@dataclass(frozen=True)
class AssetType:
    """
    Represents an asset type in the Data360 system.
    """

    uid: str
    name: str
    asset_class: AssetClass
    description: str
    auto_display_description: bool
    hierarchical: bool
    hierarchy_maximum_depth: int
    display_format: str
    notes: str
    use_as_transformation: bool
    can_own_fusion: bool
    path: str
    icon_style: dict | None
    auto_display_parent: bool | None
    can_edit_parent: bool
    is_description_enabled: bool
    is_description_visible_by_default: bool
    is_default_read_access_enabled: bool
    description_button_name: str | None


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
