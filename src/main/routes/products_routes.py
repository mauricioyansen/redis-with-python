from flask import Blueprint, jsonify

product_routes_bp = Blueprint("products_routes", __name__)


@product_routes_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"health": "ok"}), 200


@product_routes_bp.route("/products", methods=["POST"])
def insert_product():
    pass


@product_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):
    pass
