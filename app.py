from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, OpenShift! This is a Python S2I example."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
