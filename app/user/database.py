import os
import sqlite3

from app.user.models import User, UserRequest


class UserDatabase:
    def __init__(self, db_path: str) -> None:
        if db_path not in (":memory:", "file::memory:?cache=shared"):
            db_dir = os.path.dirname(db_path)
            if db_dir and not os.path.exists(db_dir):
                os.makedirs(db_dir, exist_ok=True)
        self.__conn: sqlite3.Connection | None = sqlite3.connect(db_path)
        # row_factory is available when connection is not None
        if self.__conn is not None:
            self.__conn.row_factory = sqlite3.Row
        self.__initialize_db()

    def close(self) -> None:
        if getattr(self, "_UserDatabase__conn", None):
            try:
                if self.__conn is not None:
                    self.__conn.close()
            except Exception:
                pass
            finally:
                self.__conn = None

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass

    def __get_connection(self) -> sqlite3.Connection:
        if self.__conn is None:
            raise RuntimeError("Database connection is closed")
        return self.__conn

    def __initialize_db(self) -> None:
        conn = self.__get_connection()
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
            """,
        )
        conn.commit()

    def get_all(self) -> list[User]:
        conn = self.__get_connection()
        users = conn.execute("SELECT * FROM users").fetchall()
        return [
            User(
                id=user["id"],
                name=user["name"],
                email=user["email"],
            )
            for user in users
        ]

    def exists(self, id: int) -> bool:
        conn = self.__get_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE id = ?",
            (id,),
        ).fetchone()
        return user is not None

    def get(self, id: int) -> User | None:
        conn = self.__get_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE id = ?",
            (id,),
        ).fetchone()
        if user:
            return User(
                id=user["id"],
                name=user["name"],
                email=user["email"],
            )
        return None

    def create(self, model: UserRequest) -> User | None:
        conn = self.__get_connection()
        cur = conn.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (model.name, model.email),
        )
        conn.commit()
        user_id = cur.lastrowid
        if user_id is None:
            return None
        return self.get(int(user_id))

    def update(self, id: int, model: UserRequest) -> User | None:
        conn = self.__get_connection()
        user = self.get(id)
        if not user:
            return None
        name = model.name if model.name is not None else user.name
        email = model.email if model.email is not None else user.email
        conn.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (name, email, id),
        )
        conn.commit()
        return self.get(id)

    def delete(self, id: int) -> None:
        conn = self.__get_connection()
        conn.execute("DELETE FROM users WHERE id = ?", (id,))
        conn.commit()

    def email_exists(self, email: str, exclude_id: int | None = None) -> bool:
        conn = self.__get_connection()
        if exclude_id:
            user = conn.execute(
                "SELECT * FROM users WHERE email = ? AND id != ?",
                (email, exclude_id),
            ).fetchone()
        else:
            user = conn.execute(
                "SELECT * FROM users WHERE email = ?",
                (email,),
            ).fetchone()
        return user is not None
