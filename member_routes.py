from flask import Blueprint, request, jsonify
from models.member_model import add_member, get_members
from models.log_model import log_action

member_bp = Blueprint("member_bp", __name__)

@member_bp.route("/members", methods=["POST"])
def create_member():

    data = request.json

    try:
        add_member(data)

        log_action(f"Member Added: {data['name']}")

        return jsonify({"message": "Member added"}), 201

    except:
        return jsonify({"error": "Duplicate email"}), 400


@member_bp.route("/members", methods=["GET"])
def all_members():
    return jsonify(get_members())