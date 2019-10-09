import requests
from flask import Flask, jsonify

from flask_test import __version__

app = Flask("flask_test")


@app.route("/", methods=["GET"])
def info():
    return jsonify({"version": __version__})


@app.route("/list_repositories", methods=["GET"])
def list_repositories():

    url = "https://api.github.com/repositories"
    resp = requests.get(url)
    resp = resp.json()
    resp = resp[0:5]

    return jsonify(resp)
