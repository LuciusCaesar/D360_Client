from data360.meta_model import MetaModel, MetaModelDiff


def calculate_meta_model_difference(
    target: MetaModel,
    current: MetaModel,
) -> MetaModelDiff:
    """
    Calculate the difference between two meta models.
    """
    return MetaModelDiff(
        assets_to_be_added=list(set(target.asset) - set(current.asset)),
        assets_to_be_deleted=list(set(current.asset) - set(target.asset)),
    )
