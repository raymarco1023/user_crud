from flask import (
    Flask,
    request

)
from datetime import datetime
from app.database import user

app = Flask(__name__)
VERSION = "1.0.0"


@app.get("/ping")
def ping():
    resp = {
        "status": "ok",
        "message": "success",
    }
    return resp


app.get("/version/")


def version():
    resp = {
        "status": "ok",
        "message": "success",
        "version": VERSION,
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return resp


@app.get("/users/<int:pk>")  # pk = primary key
def get_user_by_id(pk):
    target_user = user.select_by_id(pk)
    resp = {
        "status": "ok",
        "message": "success",
        "user": target_user
    }
    return resp


@app.get("/users/")
def get_all_users():
    user_list = user.scan()
    resp = {
        "status": "ok",
        "message": "success",
        "users": user_list
    }
    return resp


@app.post("/users/")
def create_user():
    user_data = request.json  # request.json coming from import "request"
    user.insert(user_data)
    return "", 204


@app.post("/users/<int:pk>")
def update_user(pk):
    user_data = request.json
    user.update(pk, user_data)
    return "", 204


@app.delete("/users/<int:pk>")
def deactive_user(pk):
    user.deactivate(pk)
    return "", 204
