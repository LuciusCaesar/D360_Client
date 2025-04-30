import random

from factory.base import Factory
from factory.faker import Faker

from data360 import model


class AssetClassFactory(Factory):
    class Meta:
        model = model.AssetClass

    id = random.randint(1, 10000)
    value = Faker("word")
    name = Faker("word")
    description = Faker("sentence")
    allow_comments_on_asset = random.choice([True, False])


class AssetTypeFactory(Factory):
    class Meta:
        model = model.AssetType

    id = random.randint(1, 10000)
    uid = Faker("word")
    name = Faker("word")
    description = Faker("sentence")
    asset_class = AssetClassFactory.build()


class AssetFactory(Factory):
    class Meta:
        model = model.Asset

    asset_id = random.randint(1, 10000)
    asset_uid = Faker("word")
    asset_type_id = random.randint(1, 10000)
    asset_type_uid = Faker("word")
    created_on = Faker("date", pattern="%Y-%m-%d")


class PredicateTypeFactory(Factory):
    class Meta:
        model = model.PredicateType

    type = Faker("word")
    name = Faker("word")
    description = Faker("sentence")


class PredicateFactory(Factory):
    class Meta:
        model = model.Predicate

    uid = Faker("word")
    name = Faker("word")
    inverse = Faker("word")
    type = PredicateTypeFactory.build()
    is_system = random.choice([True, False])
    is_in_use = random.choice([True, False])


class RelationshipTypeFactory(Factory):
    class Meta:
        model = model.RelationshipType

    id = random.randint(1, 10000)
    uid = Faker("uuid4")
    state = Faker("word")
    is_system = random.choice([True, False])
    predicate = PredicateFactory.build()
    subject = AssetTypeFactory.build()
    subject_cardinality = random.choice(list(model.Cardinality))
    object = AssetTypeFactory.build()
    object_cardinality = random.choice(list(model.Cardinality))


class RelationshipFactory(Factory):
    class Meta:
        model = model.Relationship

    uid = Faker("uuid4")
    relationship_type = RelationshipTypeFactory.build()
    state = Faker("word")
    predicate = PredicateFactory.build()
    subject = AssetFactory.build()
    object = AssetFactory.build()


class SearchFieldTypeFactory(Factory):
    class Meta:
        model = model.SearchFieldType

    add_to_result = random.choice([True, False])
    prefix = Faker("word")
    suffix = Faker("word")
    display_order = random.randint(1, 10)


class DescriptionFactory(Factory):
    class Meta:
        model = model.Description

    display = Faker("word")


class ValidationFactory(Factory):
    class Meta:
        model = model.Validation

    is_required = random.choice([True, False])


class DefinitionFieldTypeFactory(Factory):
    class Meta:
        model = model.DefinitionFieldType

    display_as_list = random.choice([True, False])
    display_assignment_source = random.choice([True, False])
    expand_group_membership = random.choice([True, False])
    responsibility_type = random.randint(1, 1000)
    responsibility_type_uid = Faker("word")


class BooleanFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.BooleanFieldTypeAttributes

    default_value = random.choice([True, False])
    description = DescriptionFactory.build()
    validation = ValidationFactory.build()
    search = SearchFieldTypeFactory.build()
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 10000)
    column_width = random.randint(1, 10000)
    sort_order = random.randint(1, 10000)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class BooleanFieldTypeFactory(Factory):
    class Meta:
        model = model.BooleanFieldType

    boolean = BooleanFieldTypeAttributesFactory.build()


class ComputedOwnershipLookupFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.ComputedOwnershipLookupFieldTypeAttributes

    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    description = DescriptionFactory.build()
    definition = DefinitionFieldTypeFactory.build()
    is_displayable = random.choice([True, False])
    is_listable = random.choice([True, False])
    show_if_empty = random.choice([True, False])
    hide_filter = random.choice([True, False])
    hide_footer = random.choice([True, False])
    hide_header = random.choice([True, False])
    display_in_column = random.choice([True, False])


class ComputedOwnershipLookupFieldTypeFactory(Factory):
    class Meta:
        model = model.ComputedOwnershipLookupFieldType

    computed_ownership_lookup = (
        ComputedOwnershipLookupFieldTypeAttributesFactory.build()
    )


class ComputedRelationshipFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.ComputedRelationshipFieldTypeAttributes

    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    description = DescriptionFactory.build()
    intersect_type_uid = Faker("uuid4")
    intersect_type_name = Faker("word")
    field_type_name = Faker("word")
    is_displayable = random.choice([True, False])
    is_listable = random.choice([True, False])
    show_if_empty = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    search = SearchFieldTypeFactory.build()
    display_in_column = random.choice([True, False])


class ComputedRelationshipFieldTypeFactory(Factory):
    class Meta:
        model = model.ComputedRelationshipFieldType

    computed_relationship = ComputedRelationshipFieldTypeAttributesFactory.build()


class ComputedRelationshipLookupFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.ComputedRelationshipLookupFieldTypeAttributes

    column_order = random.randint(1, 20)
    description = DescriptionFactory.build()
    definition = DefinitionFieldTypeFactory.build()
    is_displayable = random.choice([True, False])
    show_if_empty = random.choice([True, False])
    hide_filter = random.choice([True, False])
    hide_footer = random.choice([True, False])
    hide_header = random.choice([True, False])


class ComputedRelationshipLookupFieldTypeFactory(Factory):
    class Meta:
        model = model.ComputedRelationshipLookupFieldType

    computed_relationship_lookup = (
        ComputedRelationshipLookupFieldTypeAttributesFactory.build()
    )


class ComputedRelationshipReferenceListFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.ComputedRelationshipReferenceListFieldTypeAttributes

    column_order = random.randint(1, 20)
    description = DescriptionFactory.build()
    intersect_type_uid = Faker("uuid4")
    intersect_type_name = Faker("word")
    is_displayable = random.choice([True, False])
    show_if_empty = random.choice([True, False])
    display_ref_list_description = random.choice([True, False])


class ComputedRelationshipReferencelistFieldTypeFactory(Factory):
    class Meta:
        model = model.ComputedRelationshipReferenceListFieldType

    computed_relationship_reference_list = (
        ComputedRelationshipReferenceListFieldTypeAttributesFactory.build()
    )


class ReferenceListFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.ReferenceListFieldTypeAttributes

    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    description = DescriptionFactory.build()
    is_displayable = random.choice([True, False])
    show_if_empty = random.choice([True, False])
    display_ref_list_description = random.choice([True, False])
    display_ref_list_in_table = random.choice([True, False])
    is_listable = random.choice([True, False])


class ReferenceListFieldTypeFactory(Factory):
    class Meta:
        model = model.ReferenceListFieldType

    reference_list = ReferenceListFieldTypeAttributesFactory.build()


class CounterFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.CounterFieldTypeAttributes

    description = DescriptionFactory.build()
    search = SearchFieldTypeFactory.build()
    counter_prefix = Faker("word")
    counter_initial_index = random.randint(1, 20)
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class CounterFieldTypeFactory(Factory):
    class Meta:
        model = model.CounterFieldType

    counter = CounterFieldTypeAttributesFactory.build()


class DateFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.DateFieldTypeAttributes

    default_value = Faker("word")
    description = DescriptionFactory.build()
    validation = ValidationFactory.build()
    search = SearchFieldTypeFactory.build()
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class DateFieldTypeFactory(Factory):
    class Meta:
        model = model.DateFieldType

    date = DateFieldTypeAttributesFactory.build()


class DateTimeFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.DateTimeFieldTypeAttributes

    default_value = Faker("word")
    description = DescriptionFactory.build()
    validation = ValidationFactory.build()
    search = SearchFieldTypeFactory.build()
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class DateTimeFieldTypeFactory(Factory):
    class Meta:
        model = model.DateTimeFieldType

    date_time = DateTimeFieldTypeAttributesFactory.build()


class DecimalFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.DecimalFieldTypeAttributes

    default_value = random.random()
    description = DescriptionFactory.build()
    increment = random.random()
    validation = ValidationFactory.build()
    search = SearchFieldTypeFactory.build()
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class DecimalFieldTypeFactory(Factory):
    class Meta:
        model = model.DecimalFieldType

    decimal = DecimalFieldTypeAttributesFactory.build()


class HtmlFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.HtmlFieldTypeAttributes

    default_value = Faker("word")
    description = DescriptionFactory.build()
    validation = ValidationFactory.build()
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class HtmlFieldTypeFactory(Factory):
    class Meta:
        model = model.HtmlFieldType

    html = HtmlFieldTypeAttributesFactory.build()


class JsonFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.JsonFieldTypeAttributes

    column_order = random.randint(1, 20)
    description = DescriptionFactory.build()
    validation = ValidationFactory.build()
    is_displayable = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class JsonFieldTypeFactory(Factory):
    class Meta:
        model = model.JsonFieldType

    json_attribute = JsonFieldTypeAttributesFactory.build()


class JsonElementFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.JsonElementFieldTypeAttributes

    json_attribute = {"key": "value"}
    description = DescriptionFactory.build()
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_listable = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class JsonElementFieldTypeFactory(Factory):
    class Meta:
        model = model.JsonElementFieldType

    json_element = JsonElementFieldTypeAttributesFactory.build()


class LinkFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.LinkFieldTypeAttributes

    default_value = {"key": "value"}
    description = DescriptionFactory.build()
    validation = ValidationFactory.build()
    search = SearchFieldTypeFactory.build()
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class LinkFieldTypeFactory(Factory):
    class Meta:
        model = model.LinkFieldType

    link = LinkFieldTypeAttributesFactory.build()


class LookupFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.LookupFieldTypeAttributes

    default_value = Faker("word")
    default_formatted_value = Faker("word")
    description = DescriptionFactory.build()
    allow_all_value = random.choice([True, False])
    allow_all_label = Faker("word")
    parent_field_type_name = Faker("word")
    filter = {"key": "value"}
    format = {"key": "value"}
    list = {"key": "value"}
    validation = ValidationFactory.build()
    search = SearchFieldTypeFactory.build()
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class LookupFieldTypeFactory(Factory):
    class Meta:
        model = model.LookupFieldType

    lookup = LookupFieldTypeAttributesFactory.build()


class NumberFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.NumberFieldTypeAttributes

    default_value = random.random()
    description = DescriptionFactory.build()
    increment = random.random()
    validation = ValidationFactory.build()
    search = SearchFieldTypeFactory.build()
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class NumberFieldTypeFactory(Factory):
    class Meta:
        model = model.NumberFieldType

    number = NumberFieldTypeAttributesFactory.build()


class PathFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.PathFieldTypeAttributes

    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    description = DescriptionFactory.build()
    is_displayable = random.choice([True, False])
    is_listable = random.choice([True, False])
    display_in_column = random.choice([True, False])
    definition = {"key": "value"}


class PathFieldTypeFactory(Factory):
    class Meta:
        model = model.PathFieldType

    path = PathFieldTypeAttributesFactory.build()


class RelationshipFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.RelationshipFieldTypeAttributes

    description = DescriptionFactory.build()
    intersect_type_uid = Faker("word")
    intersect_type_name = Faker("word")
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    show_if_empty = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    display_in_column = random.choice([True, False])
    search = SearchFieldTypeFactory.build()
    use_display_format = random.choice([True, False])
    is_subject = random.choice([True, False])


class RelationshipFieldTypeFactory(Factory):
    class Meta:
        model = model.RelationshipFieldType

    relationship = RelationshipFieldTypeAttributesFactory.build()


class TextFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.TextFieldTypeAttributes

    default_value = Faker("word")
    description = DescriptionFactory.build()
    validation = ValidationFactory.build()
    search = SearchFieldTypeFactory.build()
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class TextFieldTypeFactory(Factory):
    class Meta:
        model = model.TextFieldType

    text = TextFieldTypeAttributesFactory.build()


class TagFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.TagFieldTypeAttributes

    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    description = DescriptionFactory.build()
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    tag_type_uid = Faker("uuid4")
    tag_type_id = random.randint(1, 20)


class TagFieldTypeFactory(Factory):
    class Meta:
        model = model.TagFieldType

    tag = TagFieldTypeAttributesFactory.build()


class ScoreFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.ScoreFieldTypeAttributes

    score_type = Faker("word")
    is_displayable = random.choice([True, False])
    is_listable = random.choice([True, False])
    show_if_empty = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    description = DescriptionFactory.build()
    display_in_column = random.choice([True, False])


class ScoreFieldTypeFactory(Factory):
    class Meta:
        model = model.ScoreFieldType

    score = ScoreFieldTypeAttributesFactory.build()


class SystemFieldTypeAttributesFactory(Factory):
    class Meta:
        model = model.SystemFieldTypeAttributes

    default_value = Faker("word")
    description = DescriptionFactory.build()
    validation = ValidationFactory.build()
    search = SearchFieldTypeFactory.build()
    display_in_column = random.choice([True, False])
    column_order = random.randint(1, 20)
    column_width = random.randint(1, 20)
    sort_order = random.randint(1, 20)
    sort_by_ascending = random.choice([True, False])
    is_displayable = random.choice([True, False])
    is_editable = random.choice([True, False])
    is_listable = random.choice([True, False])
    is_part_of_key = random.choice([True, False])
    is_primary_filter = random.choice([True, False])
    show_if_empty = random.choice([True, False])


class SystemFieldTypeFactory(Factory):
    class Meta:
        model = model.SystemFieldType

    system = SystemFieldTypeAttributesFactory.build()
