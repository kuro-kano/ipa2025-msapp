"""file app.py to run web server"""
from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
db = client['ipa2025_db']
routers = db["routers"]

data = []

@app.route("/")
def main():
    """main function what render index.html"""
    for x in routers.find():
        data.append(x)
    return render_template("index.html", routers=data)

@app.route("/add", methods=["POST"])
def add_router():
    """add router to data[]"""
    ip = request.form.get("ip")
    username = request.form.get("username")
    password = request.form.get("password")

    if ip and username and password:
        routers.insert_one(
            {
                "ip": ip,
                "username": username,
                "password": password
            }
        )
    return redirect("/")

@app.route("/delete/<idx>", methods=["POST"])
def delete_router(idx):
    """delete function to delete specific router"""
    idx = int(idx)

    try:
        routers.delete_one({ "_id": ObjectId(idx) })
    except Exception:
        pass

    return redirect(url_for("main"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=False)
