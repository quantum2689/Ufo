import requests
from flask import request, Flask, render_template
import json  # Import the json module

app = Flask(__name__, template_folder="temp", static_url_path="/static")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        url = request.form.get("url")
        endpoint = request.form.get("endpoint")
        htmlCode = request.form.get("htmlCode")
        json_data = request.form.get("jsonData")

        if not url or not endpoint or not htmlCode:
            # Handle missing form data
            return render_template("index.html", res="Missing form data", htmlCode="raw")

        # Parse JSON data if provided
        try:
            json_obj = json.loads(json_data) if json_data else {}
        except ValueError:
            return render_template("index.html", res="Invalid JSON data", htmlCode="raw")

        # Make the appropriate request
        if endpoint == "Get":
            response = requests.get(url)
        elif endpoint == "Post":
            response = requests.post(url, json=json_obj)
        else:
            return render_template("index.html", res="Invalid endpoint", htmlCode="raw")

        # Render the response
        return render_template("index.html", res=response.text, htmlCode=htmlCode)

if __name__ == "__main__":
    app.run(debug=True)
