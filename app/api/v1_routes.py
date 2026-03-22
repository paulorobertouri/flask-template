from flask import Blueprint, jsonify, request

from app.dependencies import get_auth_service, get_customer_service

blueprint = Blueprint("v1_routes", __name__, url_prefix="/v1")


@blueprint.get("/customer")
def list_customers():
    customers = get_customer_service().list_customers()
    return jsonify([customer.__dict__ for customer in customers])


@blueprint.get("/auth/login")
def login():
    token = get_auth_service().issue_token("demo-user")
    response = jsonify({"token": token})
    response.headers["Authorization"] = f"Bearer {token}"
    response.headers["X-JWT-Token"] = token
    return response


@blueprint.get("/public")
def public():
    return jsonify({"message": "public endpoint"})


@blueprint.get("/private")
def private():
    authorization = request.headers.get("Authorization", "")
    if not authorization.startswith("Bearer "):
        return jsonify({"detail": "Missing bearer token"}), 401

    token = authorization.removeprefix("Bearer ").strip()
    if not token:
        return jsonify({"detail": "Missing bearer token"}), 401

    try:
        payload = get_auth_service().decode_token(token)
    except Exception:  # noqa: BLE001
        return jsonify({"detail": "Invalid or expired token"}), 401

    return jsonify(
        {"message": "private endpoint", "subject": payload.get("sub")},
    )
