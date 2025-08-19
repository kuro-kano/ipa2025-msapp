"""file app.py to run web server"""
from flask import Flask, request, render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    """main function to render index.html"""
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080, threaded=False)
