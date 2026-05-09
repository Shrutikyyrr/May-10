from flask import Blueprint, request, jsonify
from models.borrow_model import borrow_book, return_book
from models.log_model import log_action

borrow_bp = Blueprint("borrow_bp", __name__)

@borrow_bp.route("/borrow", methods=["POST"])
def borrow():

    data = request.json

    result = borrow_book(
        data["member_id"],
        data["book_id"]
    )

    log_action(f"Borrow Operation Book ID: {data['book_id']}")

    return jsonify(result)


@borrow_bp.route("/return/<int:record_id>", methods=["PUT"])
def return_book_api(record_id):

    result = return_book(record_id)

    log_action(f"Return Operation Record ID: {record_id}")

    return jsonify(result)