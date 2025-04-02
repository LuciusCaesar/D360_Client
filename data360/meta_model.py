from dataclasses import dataclass

from data360.model import Asset


# meta model
@dataclass(frozen=True)
class MetaModel:
    """
    Represents a meta model in Data360
    """

    asset: list[Asset]


@dataclass(frozen=True)
class MetaModelDiff:
    """
    Represents a meta model diff in Data360
    """

    assets_to_be_added: list[Asset]
    assets_to_be_deleted: list[Asset]
