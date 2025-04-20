from dataclasses import dataclass

from data360.model import Asset, AssetType


# meta model
@dataclass(frozen=True)
class MetaModel:
    """
    Represents a meta model in Data360
    """

    asset_types: list[AssetType]
    assets: list[Asset] | None = None


@dataclass(frozen=True)
class MetaModelDiff:
    """
    Represents a meta model diff in Data360
    """

    asset_types_to_be_added: list[AssetType]
    asset_types_to_be_deleted: list[AssetType]
