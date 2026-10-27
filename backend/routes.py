from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    return jsonify(length=len(data)), 200


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    return jsonify(data), 200

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    picture = next((picture for picture in data if picture['id'] == id), None)
    if picture is None:
        abort(404)
    return jsonify(picture), 200


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    picture = request.get_json()
    if not isinstance(picture, dict) or not isinstance(picture.get('id'), int):
        return jsonify(Message='A JSON object with an integer id is required'), 400
    if any(item['id'] == picture['id'] for item in data):
        return jsonify(Message=f"picture with id {picture['id']} already present"), 302
    data.append(picture)
    return jsonify(picture), 201

######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    picture = next((picture for picture in data if picture['id'] == id), None)
    if picture is None:
        abort(404)
    update = request.get_json()
    if not isinstance(update, dict) or update.get('id', id) != id:
        return jsonify(Message='The picture id cannot change'), 400
    picture.update(update)
    return jsonify(picture), 200

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    picture = next((picture for picture in data if picture['id'] == id), None)
    if picture is None:
        abort(404)
    data.remove(picture)
    return '', 204
