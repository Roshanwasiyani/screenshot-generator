import requests
from flask_restx import Namespace, Resource
from flask import request, render_template, make_response
from src.service.screenshot_service import ScreenShotService


# Imports apis from api package
ns_screenshot = Namespace('screenshot', description='Base Template')


# Inject service (could also be dependency-injected via factory)
screenshot_service = ScreenShotService()

@ns_screenshot.route('')
class BaseTemplate(Resource):
    def get(self):
        """Render the form on GET"""
        html = render_template('index.html')
        return make_response(html)

    def post(self):
        """Handle screenshot capture on POST"""
        image_path = None

        target_url = request.form.get('url')
        format_ = request.form.get('format', 'png')
        full_page = request.form.get('full_page') == 'on'

        if not target_url:
            return render_template('index.html', error="Please enter a valid URL")

        try:
            # Send GET request to Screenshot API
            image_path = screenshot_service.capture(target_url, format_, full_page)
            print(f"Screenshot saved at: {image_path}")
        except requests.exceptions.RequestException as e:
            print(f"Error capturing screenshot: {e}")

        html = render_template('index.html', screenshot=image_path)
        return make_response(html) 