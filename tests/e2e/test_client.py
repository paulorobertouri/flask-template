import json
import os
import socket
import threading
import time
from urllib.error import URLError
from urllib.request import Request, urlopen

import pytest
import uvicorn
from playwright.sync_api import Page

from main import asgi_app


def _get_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def run_server(port: int):
    uvicorn.run(asgi_app, host="127.0.0.1", port=port, log_level="warning")


@pytest.fixture(scope="module", autouse=True)
def server():
    port = _get_free_port()
    base_url = f"http://127.0.0.1:{port}"
    thread = threading.Thread(target=run_server, args=(port,), daemon=True)
    thread.start()

    deadline = time.time() + 30
    while time.time() < deadline:
        try:
            with urlopen(f"{base_url}/health", timeout=1):
                break
        except URLError:
            time.sleep(0.2)
    else:
        raise RuntimeError("Flask test server did not become ready in time")

    yield base_url


def _get_json(url: str) -> object:
    req = Request(url, method="GET")
    with urlopen(req, timeout=3) as response:
        return json.loads(response.read().decode("utf-8"))


def _get_text(url: str) -> str:
    req = Request(url, method="GET")
    with urlopen(req, timeout=3) as response:
        return response.read().decode("utf-8")


def test_home_page_and_customer_api(server: str, page: Page):
    html = _get_text(f"{server}/static/index.html")
    assert "Flask Template Demo" in html
    assert 'id="status"' in html
    assert 'id="customers"' in html

    health = _get_json(f"{server}/health")
    assert isinstance(health, dict)
    assert health.get("status") == "ok"

    customers = _get_json(f"{server}/v1/customer")
    assert isinstance(customers, list)
    names = {c.get("name") for c in customers if isinstance(c, dict)}
    assert "Ana Flask" in names
    assert "Bruno Flask" in names

    # Capture browser evidence
    evidence_dir = "tests/e2e/evidence"
    os.makedirs(evidence_dir, exist_ok=True)
    page.goto(f"{server}/static/index.html")
    page.screenshot(path=f"{evidence_dir}/01_home_page.png", full_page=True)
