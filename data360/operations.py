from data360.meta_model import MetaModel, MetaModelDiff


def calculate_meta_model_difference(
    target: MetaModel,
    current: MetaModel,
) -> MetaModelDiff:
    """
    Calculate the difference between two meta models.
    """
    return MetaModelDiff(
        asset_types_to_be_added=list(
            set(target.asset_types) - set(current.asset_types)
        ),
        asset_types_to_be_deleted=list(
            set(current.asset_types) - set(target.asset_types)
        ),
    )
