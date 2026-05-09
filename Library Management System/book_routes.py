from flask import Blueprint, request, jsonify
from models.book_model import add_book, get_books, delete_book
from models.log_model import log_action

book_bp = Blueprint("book_bp", __name__)

@book_bp.route("/books", methods=["POST"])
def create_book():

    data = request.json

    try:
        add_book(data)
        log_action(f"Book Added: {data['title']}")

        return jsonify({"message": "Book added"}), 201

    except:
        return jsonify({"error": "Duplicate ISBN"}), 400


@book_bp.route("/books", methods=["GET"])
def all_books():
    return jsonify(get_books())


@book_bp.route("/books/<int:id>", methods=["DELETE"])
def remove_book(id):

    delete_book(id)

    log_action(f"Book Deleted: {id}")

    return jsonify({"message": "Book deleted"})