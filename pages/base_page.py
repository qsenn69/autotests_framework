from playwright.sync_api import Page, expect
from utils.config import Config

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_locator = "s__GkNOd0J0D3cppEDs s___Ih4FphCv9oj087o s__l_V_9vGK0U9NXGCh"

    def open(self, url: str):
        self.page.goto(url)

    def wait_page(self, timeout: int = None):
        if not self.base_locator:
            raise ValueError("base_locator is empty — установите self.base_locator в наследнике")
        ms_timeout = timeout if timeout is not None else int(Config.ELEMENT_SEARCH_TIMEOUT_S * 1000)
        expect(self.page.locator(self.base_locator)).to_be_visible(timeout=ms_timeout)

    def wait_for_element(self, selector: str, timeout: int = 10000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        self.page.fill(selector, value)

    def get_text(self, selector: str) -> str:
        return self.page.text_content(selector)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def assert_text(self, selector: str, expected_text: str):
        expect(self.page.locator(selector)).to_have_text(expected_text)

    def assert_url(self, expected_url: str):
        expect(self.page).to_have_url(expected_url)