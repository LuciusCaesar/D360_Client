from tests.model_factory import AssetTypeFactory


def test_asset_types_are_equals_when_their_name_is_equal():
    type1 = AssetTypeFactory.build(name="Asset Type Name")
    type2 = AssetTypeFactory.build(name="Asset Type Name")

    assert type1 == type2
    assert type1.__eq__(type2)
    assert {type1} == {type2}
    assert [type1] == [type2]
    assert set([type1]) == set([type2])


def test_asset_types_are_not_equals_when_their_name_is_not_equal():
    type1 = AssetTypeFactory.build(name="Asset Type Name A")
    type2 = AssetTypeFactory.build(name="Asset Type Name B")

    assert not type1 == type2
    assert not type1.__eq__(type2)
    assert not {type1} == {type2}
    assert not [type1] == [type2]
    assert not set([type1]) == set([type2])
