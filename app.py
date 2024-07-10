import requests
from flask import request, Flask, render_template

app = Flask(__name__, template_folder="temp", static_url_path="/static")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        url = request.form.get("url")
        endpoint = request.form.get("endpoint")
        htmlCode = request.form.get("htmlCode")
        
        if not url or not endpoint or not htmlCode:
            # Handle missing form data
            return render_template("index.html", res="Missing form data", htmlCode="raw")

        if endpoint == "Get":
            response = requests.get(url)
        elif endpoint == "Post":
            response = requests.post(url)
        else:
            return render_template("index.html", res="Invalid endpoint", htmlCode="raw")

        return render_template("index.html", res=response.text, htmlCode=htmlCode)

if __name__ == "__main__":
    app.run(debug=True)
