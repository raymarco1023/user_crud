from flask import Flask, render_template 
import requests


app = Flask(__name__)
BACKEND_URL = "http://127.0.0.1:5001"


@app.get("/")
def view_report():
    url = "%s%s" % (BACKEND_URL, "/reports/users/vehicles")
    report_data = requests.get(url)
    return render_template("index.html", results=report_data)
