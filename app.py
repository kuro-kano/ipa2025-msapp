"""file app.py to run web server"""
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

data = []

@app.route("/")
def main():
    """main function what render index.html"""
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add_comment():
    """add comment to data[]"""
    yourname = request.form.get("yourname")
    message = request.form.get("message")

    if yourname and message:
        data.append({"yourname": yourname, "message": message})
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=False)
