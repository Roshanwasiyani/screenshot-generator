import os
import requests
from src.utils.environments import Environments as ENV
from flask import url_for, current_app
from werkzeug.utils import secure_filename


class ScreenShotService:
    def __init__(self, base_url=None, api_key=None):
        self.base_url = ENV.SCREENSHOT_BASE_ENDPOINT
        self.api_key = ENV.SCREENSHOT_API_KEY

    
    def capture(self, target_url:str, format_:str = 'png', full_page:bool = False):
        """
        Capture screenshot using external API and return local saved file path.
        """
        if not target_url:
            raise ValueError("Target URL is required")

        params = {
            "url": target_url,
            "format": format_,
            "full_page": int(full_page)
        }

        headers = {"apikey": self.api_key}

        try:
            response = requests.get(
                self.base_url,
                params=params,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()

             # Safe filename
            safe_name = secure_filename(target_url.replace("://", "_").replace("/", "_"))
            image_extension = format_ if format_ != 'jpeg' else 'jpg'
            filename = f"{safe_name}.{image_extension}"

            static_dir = os.path.join(current_app.static_folder)
            os.makedirs(static_dir, exist_ok=True)

            image_path = os.path.join(static_dir, filename)
            with open(image_path, "wb") as f:
                f.write(response.content)

            print(f"Screenshot saved at: {image_path}")
            return url_for("static", filename=filename)

        except requests.exceptions.RequestException as e:
            print(f"Screenshot capture failed: {e}")
            raise RuntimeError("Screenshot capture failed") from e

