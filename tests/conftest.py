import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from utils.config import Config
import os
from pages.header import Header
from datetime import datetime

@pytest.fixture
def header(page) -> Header:
    header = Header(page)
    page.goto(Config.BASE_URL)
    header.wait_page()
    return header

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser_type = getattr(p, Config.BROWSER)
        browser = browser_type.launch(headless=Config.HEADLESS)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    yield page
    context.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            file_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=file_path, full_page=True)
            print(f"\n Screenshot saved: {file_path}")
