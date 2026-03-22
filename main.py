from os import getenv

from asgiref.wsgi import WsgiToAsgi
from dotenv import load_dotenv

from app import app as flask_app

load_dotenv()

asgi_app = WsgiToAsgi(flask_app)

if __name__ == "__main__":
    import uvicorn

    host = str(getenv("HOST")) if getenv("HOST") else "0.0.0.0"
    port = int(str(getenv("PORT"))) if getenv("PORT") else 8000
    reload = getenv("FLASK_ENV") != "production"

    uvicorn.run("main:asgi_app", host=host, port=port, reload=reload)
