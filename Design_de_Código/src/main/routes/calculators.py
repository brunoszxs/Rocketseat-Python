from flask import Blueprint, jsonify, request

calc_routp_bp = Blueprint("calc_routes", __name__)

@calc_routp_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    print(request)
    return jsonify({"sucess": True})