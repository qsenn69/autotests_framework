from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.config import Config

class Header(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.base_locator = 'div[class*="s__GkNOd0J0D3cppEDs s___Ih4FphCv9oj087o s__l_V_9vGK0U9NXGCh"]'

    def navigate_to_home(self):
        self.page.click(Config.locator("header", "logo_button"))

    def navigate_to_settings(self):
        self.page.click(Config.locator("header", "profile_button"))
        self.page.get_by_text(Config.locator("header", "settings_button")).click()
    
    def navigate_to_magazine(self):
        self.page.click(Config.locator("header", "magazine_button"))
    
    def navigate_to_support(self):
        self.page.click(Config.locator("header", "support_button"))
    
    def navigate_to_hotels(self):
        self.page.get_by_role('link', name="Отели").click()

    def navigate_to_guides(self):
        self.page.get_by_role('link', name="Коро́че").click()

    def navigate_to_favorites(self):
        self.page.get_by_role('link', name="Избранное").click()

    def navigate_to_b2b(self):
        self.page.get_by_role('link', name="Для бизнеса").click()

    def change_origin_destination(self):
        self.page.locator("button[data-test-id='round-button']").click()

    def fill_origin(self, city: str):
        self.page.locator(Config.locator("header", "origin_input")).fill(city)

    def fill_destination(self, city: str):
        self.page.locator(Config.locator("header", "destination_input")).fill(city)

    def clear_destination(self, city: str):
        self.page.locator(Config.locator("header", "destination_input")).fill(city)
        self.page.keyboard.press("Escape")

    def select_start_date(self, start_date: str):
        self.page.locator(Config.locator("header", "start_date_field")).click()
        self.page.locator(f'[data-test-id="date-{start_date}"]').click()

    def select_end_date(self, end_date: str):
        self.page.locator(Config.locator("header", "end_date_field")).click()
        self.page.locator(f'[data-test-id="date-{end_date}"]').click()

    def click_button_search(self):
        self.page.locator(Config.locator("header", "search_button")).click()

    def set_text_field_value_by_id(self, data_test_id: str, value: str):
        origin = self.page.locator(self.base_locator+'//[data-test-id="'+data_test_id+'"]")+""]')
        origin.click()
        origin.fill(value)

    def set_text_field_value_by_class(self, class_name: str, value: str):
        origin = self.page.locator('[contains(@class, "'+class_name+'")]')
        origin.click()
        origin.fill(value)