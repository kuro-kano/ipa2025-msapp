"""File app.py to run web server."""

from os import environ as env

from bson import ObjectId
from flask import Flask, redirect, render_template, request
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient(env.get("MONGO_URI"))
db = client[env.get("DB_NAME")]
routers = db["routers"]
interface_status = db["interface_status"]


@app.route("/")
def main():
    """Main function that renders index.html."""
    data = list(routers.find())
    return render_template("index.html", routers=data)


@app.route("/router/<ip>", methods=["GET"])
def router_detail(ip):
    """View router interfaces status."""
    query = {"router_ip": ip}
    data = db.interface_status.find(query).sort("timestamp", -1).limit(3)
    return render_template(
        "router.html",
        router_ip=ip,
        interface_data=data,
    )


@app.route("/add", methods=["POST"])
def add_router():
    """Add router to database."""
    ip = request.form.get("ip")
    username = request.form.get("username")
    password = request.form.get("password")

    if ip and username and password:
        router = {
            "ip": ip,
            "username": username,
            "password": password,
        }
        routers.insert_one(router)
    return redirect("/")


@app.route("/delete/<idx>", methods=["POST"])
def delete_router(idx):
    """Delete specific router from database."""
    routers.delete_one({"_id": ObjectId(idx)})
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=False)
