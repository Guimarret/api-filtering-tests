from flask import Flask, Response, jsonify, make_response, redirect, url_for, request
import json
import filtering.main

app = Flask(__name__)

@app.route("/")
def main_page():
    return redirect(url_for("routes"))

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("/routes"))

@app.route("/routes")
def routes():
    value = {
        "routes": []
    }
    return make_response(jsonify(value), 200)

@app.route("/status")
def status():
    return Response()

@app.route("/filter", methods=["POST"])
def passing_data():
    data = request.form["data"]
    columns = request.form["columns"]
    filtering(data=data, columns=columns)
    return data