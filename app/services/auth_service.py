from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from os import getenv

import jwt


@dataclass(frozen=True)
class AuthSettings:
    secret: str = getenv(
        "JWT_SECRET",
        "dev-secret-change-me-please-rotate-123456",
    )
    algorithm: str = getenv("JWT_ALGORITHM", "HS256")
    expiry_minutes: int = int(getenv("JWT_EXPIRY_MINUTES", "60"))


class AuthService:
    def __init__(self, settings: AuthSettings | None = None) -> None:
        self._settings = settings or AuthSettings()

    def issue_token(self, subject: str) -> str:
        now = datetime.now(tz=timezone.utc)
        payload = {
            "sub": subject,
            "iat": int(now.timestamp()),
            "exp": int(
                (
                    now + timedelta(minutes=self._settings.expiry_minutes)
                ).timestamp(),
            ),
        }
        return jwt.encode(
            payload,
            self._settings.secret,
            algorithm=self._settings.algorithm,
        )

    def decode_token(self, token: str) -> dict:
        return jwt.decode(
            token,
            self._settings.secret,
            algorithms=[self._settings.algorithm],
        )
