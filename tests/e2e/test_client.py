import os
import threading
import time

import pytest
import uvicorn
from playwright.sync_api import Page, expect

from main import asgi_app

SCREENSHOT_DIR = "tests/e2e/screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def run_server():
    uvicorn.run(asgi_app, host="127.0.0.1", port=8003)


@pytest.fixture(scope="module", autouse=True)
def server():
    thread = threading.Thread(target=run_server, daemon=True)
    thread.start()
    time.sleep(1)
    yield


def test_home_page_shows_customers(page: Page):
    page.goto("http://127.0.0.1:8003/static/index.html")

    heading = page.get_by_role("heading", name="Flask Template Demo")
    expect(heading).to_be_visible()
    expect(page.locator("#status")).to_have_text("ok")
    expect(page.get_by_text("Ana Flask")).to_be_visible()
    expect(page.get_by_text("Bruno Flask")).to_be_visible()

    page.screenshot(path=f"{SCREENSHOT_DIR}/home_page.png")
