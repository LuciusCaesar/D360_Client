from config import AppConfig
from data360.client import Data360Instance

if __name__ == "__main__":
    # Load configuration
    config = AppConfig()

    # Create the Data360 instance to work on a final environment
    data360 = Data360Instance(
        url=config.SOURCE_URL,
        api_key=config.SOURCE_API_KEY.get_secret_value(),
        api_secret=config.SOURCE_API_SECRET.get_secret_value(),
    )
    data360.loadMetamodel()
    print(data360.metamodel)
