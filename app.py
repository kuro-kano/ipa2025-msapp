"""file app.py to run web server"""
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    """main function to render index.html"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=False)
