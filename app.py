from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <-- This enables CORS for all routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
