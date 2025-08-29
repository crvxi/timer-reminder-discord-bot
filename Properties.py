import os
from dotenv import load_dotenv


class Properties:
    """
    A Singleton class to load and provide configuration properties from a .env file.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Properties, cls).__new__(cls)
            cls._instance._load_properties()
        return cls._instance

    def _load_properties(self):
        """
        Loads properties from the .env file and sets them as attributes.
        """
        load_dotenv()
        self.TOKEN = os.getenv('DISCORD_TOKEN')
        self.SERVER_ID = int(os.getenv('SERVER_ID'))

    def get_property(self, property_name):
        """
        A generic method to get a property by its name.
        """
        return getattr(self, property_name, None)
