from app import app


def test_v1_customer_auth_public_private_and_swagger() -> None:
    client = app.test_client()

    swagger_response = client.get("/apidocs/")
    assert swagger_response.status_code == 200

    customer_response = client.get("/v1/customer")
    assert customer_response.status_code == 200
    assert isinstance(customer_response.get_json(), list)

    login_response = client.get("/v1/auth/login")
    assert login_response.status_code == 200
    auth_header = login_response.headers.get("Authorization")
    assert auth_header is not None

    public_response = client.get("/v1/public")
    assert public_response.status_code == 200

    private_response = client.get(
        "/v1/private",
        headers={"Authorization": auth_header},
    )
    assert private_response.status_code == 200
