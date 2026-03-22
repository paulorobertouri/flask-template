from app.services.auth_service import AuthService


def test_issue_and_decode_token() -> None:
    service = AuthService()

    token = service.issue_token("unit-user")
    payload = service.decode_token(token)

    assert payload["sub"] == "unit-user"
