from flask import Blueprint, jsonify, request
from src.http_types.http_req import HttpReq
from src.main.composer.product_creator_composer import product_creator_composer
from src.main.composer.product_finder_composer import product_finder_composer

product_routes_bp = Blueprint("products_routes", __name__)


@product_routes_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"health": "ok"}), 200


@product_routes_bp.route("/products", methods=["POST"])
def insert_product():
    req = HttpReq(body=request.json)
    product_creator = product_creator_composer()
    res = product_creator.create(req)
    return jsonify(res.body), res.status_code


@product_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):
    req = HttpReq(params={"product_name": product_name})
    product_finder = product_finder_composer()
    res = product_finder.find_by_name(req)
    return jsonify(res.body), res.status_code
