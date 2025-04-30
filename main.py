from config import AppConfig
from data360.client import Data360Instance

if __name__ == "__main__":
    # Load configuration
    config = AppConfig()

    # Create the Data360 instance to work on a final environment
    source = Data360Instance(
        url=config.SOURCE_URL,
        api_key=config.SOURCE_API_KEY.get_secret_value(),
        api_secret=config.SOURCE_API_SECRET.get_secret_value(),
    )
    destination = Data360Instance(
        url=config.DESTINATION_URL,
        api_key=config.DESTINATION_API_KEY.get_secret_value(),
        api_secret=config.DESTINATION_API_SECRET.get_secret_value(),
    )

    print("")
    print("source asset_types")
    print(len(source.asset_types))
    print([asset_type.name for asset_type in source.asset_types])

    print("")
    print("destination asset_types")
    print(len(destination.asset_types))
    print([asset_type.name for asset_type in destination.asset_types])

    asset_types_not_in_source = list(
        set(destination.asset_types) - set(source.asset_types)
    )
    asset_types_not_in_dest = list(
        set(source.asset_types) - set(destination.asset_types)
    )

    print("")
    print("asset types not in source")
    print(len(asset_types_not_in_source))
    print([type.name for type in asset_types_not_in_source])

    print("")
    print("asset types not in destination")
    print(len(asset_types_not_in_dest))
    print([asset.name for asset in asset_types_not_in_dest])

    # print(source.fields)
