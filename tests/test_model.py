from data360.model import AssetClass, AssetClassName, AssetType


def test_asset_types_are_equals_when_their_name_is_equal():
    type1 = AssetType(
        id="1234567890",
        uid="1234567890",
        name="Test Asset Type",
        asset_class=AssetClass(
            id="0987654321",
            value="Test Asset Class",
            name=AssetClassName.BUSINESS_ASSET,
            description="Test Asset Class Description",
            allow_comments_on_asset=True,
        ),
        description="Test Asset Type Description",
        auto_display_description=True,
        hierarchical=False,
        hierarchy_maximum_depth=0,
        display_format="Test Display Format",
        notes="Test Notes",
        use_as_transformation=False,
        can_own_fusion=False,
        path="Test Path",
        can_edit_parent=False,
        is_description_enabled=True,
        is_description_visible_by_default=True,
        is_default_read_access_enabled=True,
    )

    type2 = AssetType(
        id="40594",
        uid="52600",
        name="Test Asset Type",
        asset_class=AssetClass(
            id="0987654321",
            value="Test Asset Class",
            name=AssetClassName.BUSINESS_ASSET,
            description="Test Asset Class Description",
            allow_comments_on_asset=True,
        ),
        description="Test Asset Type Description",
        auto_display_description=True,
        hierarchical=False,
        hierarchy_maximum_depth=0,
        display_format="Test Display Format",
        notes="Test Notes",
        use_as_transformation=False,
        can_own_fusion=False,
        path="Test Path",
        can_edit_parent=False,
        is_description_enabled=True,
        is_description_visible_by_default=True,
        is_default_read_access_enabled=True,
    )

    assert type1 == type2
    assert type1.__eq__(type2)
    assert {type1} == {type2}
    assert [type1] == [type2]
    assert set([type1]) == set([type2])
