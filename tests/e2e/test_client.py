import os
import socket
import threading
import time
from urllib.error import URLError
from urllib.request import urlopen

import pytest
import uvicorn
from playwright.sync_api import Page, expect

from main import asgi_app

SCREENSHOT_DIR = "tests/e2e/screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


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


def test_home_page_shows_customers(page: Page, server: str):
    page.goto(f"{server}/static/index.html")

    # Wait for the page to load and initial scripts to run
    page.wait_for_load_state("networkidle")

    # Verify heading is present
    heading = page.get_by_role("heading", name="Flask Template Demo")
    expect(heading).to_be_visible()

    # Wait for status API call to complete
    status = page.locator("#status")
    expect(status).not_to_have_text("Checking...", timeout=15_000)
    expect(status).to_have_text("ok", timeout=15_000)

    # Once status is "ok", customers should be loaded too
    customers = page.locator("#customers .card")
    expect(customers).to_have_count(2, timeout=5_000)
    expect(page.get_by_text("Ana Flask")).to_be_visible(timeout=5_000)
    expect(page.get_by_text("Bruno Flask")).to_be_visible(timeout=5_000)

    page.screenshot(path=f"{SCREENSHOT_DIR}/home_page.png")
