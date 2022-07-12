from flask import Flask, redirect, url_for,render_template, json
import os
app = Flask(__name__)

@app.route("/")
def home():
    SITE_ROOT = os.path.relpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "listOfUsers.json")
    data = json.load(open(json_url))
    
    SITE_ROOT = os.path.relpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "keywordCloud.json")
    cloud = json.load(open(json_url))
    return render_template("index.html", data=data, cloud=cloud)


if __name__ == "__main__":
    app.run()