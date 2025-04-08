from data360 import model, operations
from data360.meta_model import MetaModel


def test_asset_diff():
    # Set up test
    asset1 = model.Asset(
        AssetId=1,
        AssetUid="asset1",
        Name="Asset 1",
        XrefId="ref1",
        AssetTypeId=1,
        AssetTypeUid="type1",
        UpdatedOn="2023-10-01T00:00:00Z",
        CreatedOn="2023-10-01T00:00:00Z",
        Color="red",
        Path="/path/to/asset1",
        DisplayPath="/display/path/to/asset1",
        BusinessTerm="Business Term 1",
        DataPoint="Data Point 1",
        BusinessTermDefinition="Business Term Definition 1",
        DataPointDefinition="Data Point Definition 1",
        Key="Key 1",
        DataPrivacyType="Data Privacy Type 1",
        Integrity="Integrity 1",
        Confidentiality="Confidentiality 1",
        QltyScore="Quality Score 1",
        Critical="Critical 1",
        GovernanceScore="Governance Score 1",
        Suggestedcritical="Suggested Critical 1",
        DataClassifiedBy="Data Classified By 1",
    )
    asset2 = model.Asset(
        AssetId=2,
        AssetUid="asset2",
        Name="Asset 2",
        XrefId="ref2",
        AssetTypeId=1,
        AssetTypeUid="type2",
        UpdatedOn="2023-20-01T00:00:00Z",
        CreatedOn="2023-20-01T00:00:00Z",
        Color="red",
        Path="/path/to/asset2",
        DisplayPath="/display/path/to/asset2",
        BusinessTerm="Business Term 2",
        DataPoint="Data Point 2",
        BusinessTermDefinition="Business Term Definition 2",
        DataPointDefinition="Data Point Definition 2",
        Key="Key 2",
        DataPrivacyType="Data Privacy Type 2",
        Integrity="Integrity 2",
        Confidentiality="Confidentiality 2",
        QltyScore="Quality Score 2",
        Critical="Critical 2",
        GovernanceScore="Governance Score 2",
        Suggestedcritical="Suggested Critical 2",
        DataClassifiedBy="Data Classified By 2",
    )
    asset3 = model.Asset(
        AssetId=3,
        AssetUid="asset3",
        Name="Asset 3",
        XrefId="ref3",
        AssetTypeId=3,
        AssetTypeUid="type3",
        UpdatedOn="2023-30-01T00:00:00Z",
        CreatedOn="2023-30-01T00:00:00Z",
        Color="red",
        Path="/path/to/asset3",
        DisplayPath="/display/path/to/asset3",
        BusinessTerm="Business Term 3",
        DataPoint="Data Point 3",
        BusinessTermDefinition="Business Term Definition 3",
        DataPointDefinition="Data Point Definition 3",
        Key="Key 3",
        DataPrivacyType="Data Privacy Type 3",
        Integrity="Integrity 3",
        Confidentiality="Confidentiality 3",
        QltyScore="Quality Score 3",
        Critical="Critical 3",
        GovernanceScore="Governance Score 3",
        Suggestedcritical="Suggested Critical 3",
        DataClassifiedBy="Data Classified By 3",
    )

    targetMetaModel = MetaModel(
        asset=[
            asset1,
            asset2,
        ]
    )

    sourceMetaModel = MetaModel(
        asset=[
            asset1,
            asset3,
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
    assert diff.assets_to_be_added == [asset2]
    assert diff.assets_to_be_deleted == [asset3]
