import requests
import os
from flask_restx import Namespace, Resource
from flask import request, render_template, make_response
from utils.environments import Environments as ENV

# Imports apis from api package
ns_base_template = Namespace('screenshot', description='Base Template')


@ns_base_template.route('')
class BaseTemplate(Resource):
    def get(self):
        """Render the form on GET"""
        html = render_template('index.html')
        return make_response(html)

    def post(self):
        """Handle screenshot capture on POST"""
        screenshot_url = None

        target_url = request.form.get('url')
        format_ = request.form.get('format', 'png')
        full_page = request.form.get('full_page') == 'on'

        if not target_url:
            return render_template('index.html', error="Please enter a valid URL")

        params = {
            "url": target_url,
            "format": format_,
            "full_page": int(full_page)
        }
        headers = {"apikey": ENV.SCREENSHOT_API_KEY}

        try:
            # Send GET request to Screenshot API
            response = requests.get(
                ENV.SCREENSHOT_BASE_ENDPOINT,
                params=params,
                headers=headers,
                timeout=30
            )
            response.raise_for_status()

            # Save the returned image in /static
            image_extension = format_ if format_ != 'jpeg' else 'jpg'
            image_path = os.path.join('static', f'{target_url.split(".com")[0].split("://")[1]}.{image_extension}')
            with open(image_path, 'wb') as f:
                f.write(response.content)

            screenshot_url = image_path

        except requests.exceptions.RequestException as e:
            print(f"Error capturing screenshot: {e}")

        html = render_template('index.html', screenshot=screenshot_url)
        return make_response(html) 