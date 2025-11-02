Screenshot Generator

A simple web application that allows users to generate screenshots of any web page by entering its URL.
The app sends the URL to a backend API, which uses a third-party screenshot service to capture the webpage and display it back in the UI.


Features:

-- Clean and minimal user interface
-- Accepts any valid website URL
-- Uses third-party API to capture screenshots
-- Displays the generated screenshot instantly in the UI
-- Responsive design for desktop and mobile


Project Architecture: 

Frontend (HTML + JS UI)
        │
        ▼
Backend (Flask API)
        │
        ▼
Third-Party Screenshot API (Screenshotbase)


Installation & Setup: 

1. Clone the Repository
git clone https://github.com/Roshanwasiyani/screenshot-generator.git
cd screenshot-generator

2. Create a Virtual Environment (Optional but Recommended)
python -m venv .venv
.venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Flask Server
python app.py

5. Open in Browser

Check Health of server: http://localhost:5000/api/v1/health-check
Go to: http://localhost:5000/api/v1/screenshot

🔑 Environment Variables

Create a .env file in the project root with your third-party API credentials:

SCREENSHOT_BASE_ENDPOINT= 
SCREENSHOT_API_KEY = 

How It Works

User enters a URL in the input field.

The app sends a POST request to the backend Flask route (/screenshot).

The backend calls the third-party Screenshot API with the given URL.

The API returns the screenshot image link or base64 data.

The UI updates and displays the screenshot to the user.



Folder Structure: 

screenshot-generator/
├── app.py
├── src
    └── api
        └── __init__.py
        └── screenshot_api.py
        └── health_check_api.py
    └── service
        └── __init__.py
        └── screenshot_service.py
    └── utils
        └── __init__.py
        └── enviornments.py
    └── static
        └── {Contains ScreenShots}
    └── templates
        └── index.html
├── requirements.txt
├── .env
├── .env.sample {Contain sample keys for Environment Variables}
└── README.md
