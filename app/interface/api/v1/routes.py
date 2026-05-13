from flask import Blueprint, jsonify, request
from app.core.dependencies import get_auth_service, get_list_customers_use_case

v1_bp = Blueprint('v1', __name__)

@v1_bp.route('/customer', methods=['GET'])
def list_customers():
    use_case = get_list_customers_use_case()
    customers = use_case.execute()
    return jsonify([c.model_dump() for c in customers])

@v1_bp.route('/auth/login', methods=['GET'])
def login():
    token = get_auth_service().issue_token("demo-user")
    return jsonify({"token": token}), 200, {
        "Authorization": f"Bearer {token}",
        "X-JWT-Token": token
    }

@v1_bp.route('/public', methods=['GET'])
def public():
    return jsonify({"message": "public endpoint"})
