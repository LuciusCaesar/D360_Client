from data360 import model, operations
from data360.meta_model import MetaModel


def test_asset_diff():
    # Set up test
    asset_type_1 = model.AssetType(
        id=1,
        uid="asset_type_1",
        name="Asset Type 1",
        asset_class=model.AssetClass(
            id=1,
            value="asset_type_1",
            name="Asset Type 1",
            description="Description of Asset Type 1",
            allow_comments_on_asset=True,
        ),
        description="Description of Asset Type 1",
    )
    asset_type_2 = model.AssetType(
        id=2,
        uid="asset_type_2",
        name="Asset Type 2",
        asset_class=model.AssetClass(
            id=2,
            value="asset_type_2",
            name="Asset Type 2",
            description="Description of Asset Type 2",
            allow_comments_on_asset=True,
        ),
        description="Description of Asset Type 2",
    )
    asset_type_3 = model.AssetType(
        id=3,
        uid="asset_type_3",
        name="Asset Type 3",
        asset_class=model.AssetClass(
            id=3,
            value="asset_type_3",
            name="Asset Type 3",
            description="Description of Asset Type 3",
            allow_comments_on_asset=True,
        ),
        description="Description of Asset Type 3",
    )

    targetMetaModel = MetaModel(
        asset_types=[
            asset_type_1,
            asset_type_2,
        ]
    )

    sourceMetaModel = MetaModel(
        asset_types=[
            asset_type_1,
            asset_type_3,
        ]
    )

    # test
    diff = operations.calculate_meta_model_difference(
        target=targetMetaModel,
        current=sourceMetaModel,
    )
    # Assert the diff
    # assertEqual(diff.assets_to_be_added, [asset2])
    # assertEqual(diff.assets_to_be_deleted, [asset3])
    assert diff.asset_types_to_be_added == [asset_type_2]
    assert diff.asset_types_to_be_deleted == [asset_type_3]
