import os
from dotenv import load_dotenv

load_dotenv(".env")


class Environments:
    SCREENSHOT_BASE_ENDPOINT = os.environ.get("SCREENSHOT_BASE_ENDPOINT")
    SCREENSHOT_API_KEY = os.environ.get("SCREENSHOT_API_KEY")
