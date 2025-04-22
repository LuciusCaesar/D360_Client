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
        if not isinstance(other, AssetType):
            return NotImplemented
        # Compare all fields except 'id'
        return self.name == other.name

    def __hash__(self):
        # Hash only the fields used in __eq__
        return hash((self.name))


class Asset(PascalCaseObject):
    """
    Represents an asset in the Data360 system.
    """

    asset_id: int
    asset_uid: str
    xref_id: str | None = None
    asset_type_id: int
    asset_type_uid: str
    updated_on: str | None = None
    created_on: str
    color: str | None = None
    path: str | None = None
    display_path: str | None = None
    name: str | None = None
    business_term: str | None = None
    data_point: str | None = None
    business_term_definition: str | None = None
    data_point_definition: str | None = None
    key: str | None = None
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


class Cardinality(Enum):
    """
    Enum representing the cardinality of relationships in the Data360 system.
    """

    ONE = "One"
    MANY = "Many"


class PredicateType(PascalCaseObject):
    """
    Enum representing the names of predicate types in the Data360 system.
    """

    type: str
    name: str
    description: str


class Predicate(PascalCaseObject):
    uid: str
    name: str
    inverse: str
    type: PredicateType
    is_system: bool
    is_in_use: bool


class RelationshipType(PascalCaseObject):
    """
    Represents a relationship type in the Data360 system.
    """

    id: int
    uid: str
    state: str
    is_system: bool
    predicate: Predicate
    subject: AssetType
    subject_cardinality: Cardinality
    object: AssetType
    object_cardinality: Cardinality


class Relationship(PascalCaseObject):
    """
    Represents a relationship in the Data360 system.
    """

    uid: str
    relationship_type: RelationshipType
    state: str
    predicate: Predicate
    subject: Asset
    object: Asset


class SearchFieldType(PascalCaseObject):
    """
    Represents a search field type in the Data360 system.
    """

    add_to_result: bool | None = None
    prefix: str | None = None
    suffix: str | None = None
    display_order: int | None = None


class Description(PascalCaseObject):
    display: str
    form: str | None = None


class Validation(PascalCaseObject):
    is_required: bool
    precision: int | None = None
    minimum_value: int | None = None
    maximum_value: int | None = None
    minimum_length: int | None = None
    maximum_length: int | None = None
    message: str | None = None
    pattern: str | None = None


class DefinitionFieldType(PascalCaseObject):
    """
    Represents a definition type in the Data360 system.
    """

    display_as_list: bool
    display_assignment_source: bool
    expand_group_membership: bool
    responsibility_type: int
    responsibility_type_uid: str


class BooleanFieldTypeAttributes(PascalCaseObject):
    """
    Represents a Boolean field type in the Data360 system.
    """

    default_value: bool
    description: Description
    validation: Validation
    search: SearchFieldType
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class BooleanFieldType(PascalCaseObject):
    boolean: BooleanFieldTypeAttributes


class ComputedOwnershipLookupFieldTypeAttributes(PascalCaseObject):
    """
    Represents a computed ownership lookup field type in the Data360 system.
    """

    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    description: Description
    definition: DefinitionFieldType
    is_displayable: bool
    is_listable: bool
    show_if_empty: bool
    hide_filter: bool
    hide_footer: bool
    hide_header: bool
    display_in_column: bool


class ComputedOwnershipLookupFieldType(PascalCaseObject):
    computed_ownership_lookup: ComputedOwnershipLookupFieldTypeAttributes


class ComputedRelationshipFieldTypeAttributes(PascalCaseObject):
    """
    Represents a computed relationship field type in the Data360 system.
    """

    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    description: Description
    intersect_type_uid: str
    intersect_type_name: str
    field_type_name: str
    is_displayable: bool
    is_listable: bool
    show_if_empty: bool
    is_primary_filter: bool
    search: SearchFieldType
    display_in_column: bool


class ComputedRelationshipFieldType(PascalCaseObject):
    computed_relationship: ComputedRelationshipFieldTypeAttributes


class ComputedRelationshipLookupFieldTypeAttributes(PascalCaseObject):
    """
    Represents a computed relationship lookup field type in the Data360 system.
    """

    column_order: int
    description: Description
    definition: dict
    is_displayable: bool
    show_if_empty: bool
    hide_filter: bool
    hide_footer: bool
    hide_header: bool


class ComputedRelationshipLookupFieldType(PascalCaseObject):
    computed_relationship_lookup: ComputedRelationshipLookupFieldTypeAttributes


class ComputedRelationshipReferenceListFieldTypeAttributes(PascalCaseObject):
    """
    Represents a computed relationship reference list field type in the Data360 system.
    """

    column_order: int
    description: Description
    intersect_type_uid: str
    intersect_type_name: str
    is_displayable: bool
    show_if_empty: bool
    display_ref_list_description: bool


class ComputedRelationshipReferenceListFieldType(PascalCaseObject):
    computed_relationship_reference_list: (
        ComputedRelationshipReferenceListFieldTypeAttributes
    )


class ReferenceListFieldTypeAttributes(PascalCaseObject):
    """
    Represents a reference list field type in the Data360 system.
    """

    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    description: Description
    is_displayable: bool
    show_if_empty: bool
    display_ref_list_description: bool
    display_ref_list_in_table: bool
    is_listable: bool


class ReferenceListFieldType(PascalCaseObject):
    reference_list: ReferenceListFieldTypeAttributes


class CounterFieldTypeAttributes(PascalCaseObject):
    """
    Represents a counter field type in the Data360 system.
    """

    description: Description
    search: SearchFieldType
    counter_prefix: str
    counter_initial_index: int
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class CounterFieldType(PascalCaseObject):
    Counter: CounterFieldTypeAttributes


class DateFieldTypeAttributes(PascalCaseObject):
    """
    Represents a date field type in the Data360 system.
    """

    default_value: str
    description: Description
    validation: Validation
    search: SearchFieldType
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class DateFieldType(PascalCaseObject):
    Date: DateFieldTypeAttributes


class DateTimeFieldTypeAttributes(PascalCaseObject):
    """
    Represents a date-time field type in the Data360 system.
    """

    default_value: str
    description: Description
    validation: Validation
    search: SearchFieldType
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class DateTimeFieldType(PascalCaseObject):
    date_time: DateTimeFieldTypeAttributes


class DecimalFieldTypeAttributes(PascalCaseObject):
    """
    Represents a decimal field type in the Data360 system.
    """

    default_value: float
    description: Description
    increment: float
    validation: Validation
    search: SearchFieldType
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class DecimalFieldType(PascalCaseObject):
    decimal: DecimalFieldTypeAttributes


class HtmlFieldTypeAttributes(PascalCaseObject):
    """
    Represents an HTML field type in the Data360 system.
    """

    default_value: str
    description: Description
    validation: Validation
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class HtmlFieldType(PascalCaseObject):
    html: HtmlFieldTypeAttributes


class JsonFieldTypeAttributes(PascalCaseObject):
    """
    Represents a JSON field type in the Data360 system.
    """

    column_order: int
    description: Description
    validation: Validation
    is_displayable: bool
    show_if_empty: bool


class JsonFieldType(PascalCaseObject):
    json_attribute: JsonFieldTypeAttributes = Field(
        alias="Json"
    )  # For some reasons, mypy doesn't like when the attribute is called "json" only.


class JsonElementFieldTypeAttributes(PascalCaseObject):
    """
    Represents a JSON element field type in the Data360 system.
    """

    json_attribute: dict
    description: Description
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_listable: bool
    show_if_empty: bool


class JsonElementFieldType(PascalCaseObject):
    json_element: JsonElementFieldTypeAttributes


class LinkFieldTypeAttributes(PascalCaseObject):
    """
    Represents a link field type in the Data360 system.
    """

    default_value: dict
    description: Description
    validation: Validation
    search: SearchFieldType
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class LinkFieldType(PascalCaseObject):
    link: LinkFieldTypeAttributes


class LookupFieldTypeAttributes(PascalCaseObject):
    """
    Represents a lookup field type in the Data360 system.
    """

    default_value: str
    default_formatted_value: str
    description: Description
    allow_all_value: bool
    allow_all_label: str
    parent_field_type_name: str
    filter: dict
    format: dict
    list: dict
    validation: Validation
    search: SearchFieldType
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class LookupFieldType(PascalCaseObject):
    lookup: LookupFieldTypeAttributes


class NumberFieldTypeAttributes(PascalCaseObject):
    """
    Represents a number field type in the Data360 system.
    """

    default_value: float
    description: Description
    increment: float
    validation: Validation
    search: SearchFieldType
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class NumberFieldType(PascalCaseObject):
    number: NumberFieldTypeAttributes


class PathFieldTypeAttributes(PascalCaseObject):
    """
    Represents a path field type in the Data360 system.
    """

    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    description: Description
    is_displayable: bool
    is_listable: bool
    display_in_column: bool
    definition: dict


class PathFieldType(PascalCaseObject):
    path: PathFieldTypeAttributes


class RelationshipFieldTypeAttributes(PascalCaseObject):
    """
    Represents a relationship field type in the Data360 system.
    """

    description: Description
    intersect_type_uid: str
    intersect_type_name: str
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    show_if_empty: bool
    is_primary_filter: bool
    display_in_column: bool
    search: SearchFieldType
    use_display_format: bool
    is_subject: bool


class RelationshipFieldType(PascalCaseObject):
    relationship: RelationshipFieldTypeAttributes


class TextFieldTypeAttributes(PascalCaseObject):
    """
    Represents a text field type in the Data360 system.
    """

    default_value: str
    description: Description
    validation: Validation
    search: SearchFieldType
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class TextFieldType(PascalCaseObject):
    text: TextFieldTypeAttributes


class TagFieldTypeAttributes(PascalCaseObject):
    """
    Represents a tag field type in the Data360 system.
    """

    column_order: int
    column_width: int
    description: Description
    sort_order: int
    sort_by_ascending: bool
    is_listable: bool
    is_primary_filter: bool
    tag_type_uid: str = Field(alias="TagTypeUID")
    tag_type_id: int = Field(alias="TagTypeID")


class TagFieldType(PascalCaseObject):
    tag: TagFieldTypeAttributes


class ScoreFieldTypeAttributes(PascalCaseObject):
    """
    Represents a score field type in the Data360 system.
    """

    score_type: str
    is_displayable: bool
    is_listable: bool
    show_if_empty: bool
    is_primary_filter: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    description: Description
    display_in_column: bool


class ScoreFieldType(PascalCaseObject):
    score: ScoreFieldTypeAttributes


class SystemFieldTypeAttributes(PascalCaseObject):
    """
    Represents a system field type in the Data360 system.
    """

    default_value: str
    description: Description
    validation: Validation
    search: SearchFieldType
    display_in_column: bool
    column_order: int
    column_width: int
    sort_order: int
    sort_by_ascending: bool
    is_displayable: bool
    is_editable: bool
    is_listable: bool
    is_part_of_key: bool
    is_primary_filter: bool
    show_if_empty: bool


class SystemFieldType(PascalCaseObject):
    system: SystemFieldTypeAttributes


class FieldAsset(PascalCaseObject):
    """
    Represents a field in the Data360 system.
    """

    name: str
    friendly_name: str
    category: str
    action_type_uid: str | None = None
    asset_type_uid: str
    relationship_type_uid: str | None = None
    id: int | None = None
    type: (
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
        | None
    )
