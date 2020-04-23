#!/usr/bin/env python3

"""Python is life"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, welcome To My Domain... <h1>Blaqhut Projects!<h1>"

if __name__ == "__main__":
    app.run()
