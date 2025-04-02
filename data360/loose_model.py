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


class AssetClass:
    """
    Represents an asset class in the Data360 system.
    """

    def __init__(self, **kwargs):
        """
        Initialize an AssetClass object with the given attributes.
        :param kwargs: The attributes of the asset.
        """
        self.__dict__.update(kwargs)


class AssetType:
    """
    Represents an asset type in the Data360 system.
    """

    def __init__(self, **kwargs):
        """
        Initialize an AssetType object with the given attributes.
        :param kwargs: The attributes of the asset.
        """
        self.__dict__.update(kwargs)


# @dataclass(frozen=True)
class Asset:
    """
    Represents an asset in the Data360 system.
    """

    def __init__(self, **kwargs):
        """
        Initialize an Asset object with the given attributes.
        :param kwargs: The attributes of the asset.
        """
        self.__dict__.update(kwargs)


# Relationships
class Cardinality(Enum):
    """
    Enum representing the cardinality of relationships in the Data360 system.
    """

    ONE = "One"
    MANY = "Many"


class PredicateType:
    """
    Enum representing the names of predicate types in the Data360 system.
    """

    def __init__(self, **kwargs):
        """
        Initialize a PredicateType object with the given attributes.
        :param kwargs: The attributes of the predicate type.
        """
        self.__dict__.update(kwargs)


class Predicate:
    """
    Represents a predicate in the Data360 system.
    """

    def __init__(self, **kwargs):
        """
        Initialize a Predicate object with the given attributes.
        :param kwargs: The attributes of the predicate.
        """
        self.__dict__.update(kwargs)


class RelationshipType:
    """
    Represents a relationship type in the Data360 system.
    """

    def __init__(self, **kwargs):
        """
        Initialize a RelationshipType object with the given attributes.
        :param kwargs: The attributes of the relationship type.
        """
        self.__dict__.update(kwargs)


class Relationship:
    """
    Represents a relationship in the Data360 system.
    """

    def __init__(self, **kwargs):
        """
        Initialize a Relationship object with the given attributes.
        :param kwargs: The attributes of the relationship.
        """
        self.__dict__.update(kwargs)


class Field:
    """
    Represents a field in the Data360 system.
    """

    def __init__(self, **kwargs):
        """
        Initialize a Field object with the given attributes.
        :param kwargs: The attributes of the field.
        """
        self.__dict__.update(kwargs)
