"""
You run this script by executing python app.py/ gunicorn 'app:app' in the terminal.
The Flask app starts a local web server (by default on localhost:5000).
When you navigate to http://localhost:5000/ in your web browser, Flask matches the route (/) to the home() function.
The home() function returns the text "Hello World", which is sent as the HTTP response to the browser.
Your browser displays "Hello World" on the page.
This is the basic structure of a Flask application. As you add more routes and logic, Flask will match the URLs you visit to different functions and handle more complex logic!
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Breast Cancer Prediction!'

if __name__ == '__main__':
    app.run(debug=False)
