import json

from config import AppConfig
from data360.client import Data360Instance
from data360.operations import update_attributes

if __name__ == "__main__":
    # Load configuration
    config = AppConfig()

    # Create the Data360 instance to work on a final environment
    data360 = Data360Instance(
        config.SOURCE_URL,
        config.SOURCE_API_KEY.get_secret_value(),
        config.SOURCE_API_SECRET.get_secret_value(),
    )

    fields = data360.get_fields_by_asset_type_uid(
        "6e40b7cd-30ed-4e91-9b4c-ab9050943f3c"
    )

    update_attributes("AssetTypeUid", "test_uid", fields)
    print(json.dumps([item.__dict__ for item in fields], indent=4))
