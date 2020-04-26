import os
from dotenv import load_dotenv
from automation.utils import decode


load_dotenv()


APPLICATION_SECRET_KEY = os.getenv("SECRET_KEY")

SKYPE_USERNAME = decode(os.getenv("SKYPE_USERNAME"), "username",
                        APPLICATION_SECRET_KEY)
SKYPE_PASSWORD = decode(os.getenv("SKYPE_PASSWORD"), "password",
                        APPLICATION_SECRET_KEY)

EXAMPLE_GROUP_ID = decode(os.getenv("EXAMPLE_GROUP"), "channel_id",
                          APPLICATION_SECRET_KEY)
TARGET_GROUP_ID = decode(os.getenv("TARGET_GROUP"), "channel_id",
                         APPLICATION_SECRET_KEY)
