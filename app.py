"""file app.py to run web server"""
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

data = []

@app.route("/")
def main():
    """main function what render index.html"""
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add_router():
    """add router to data[]"""
    ip = request.form.get("ip")
    username = request.form.get("username")

    if ip and username:
        data.append({"ip": ip, "username": username})
    return redirect("/")

@app.route("/delete/<idx>", methods=["POST"])
def delete_router(idx):
    """delete function to delete specific router"""
    idx = int(idx)

    try:
        if 0 <= idx < len(data):
            data.pop(idx)
    except Exception:
        pass

    return redirect(url_for("main"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=False)
