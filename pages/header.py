from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.selectors import HeaderSelectors

class Header(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.base_locator = 'div[class*="s__GkNOd0J0D3cppEDs s___Ih4FphCv9oj087o s__l_V_9vGK0U9NXGCh"]'

    def navigate_to_home(self):
        self.page.click(HeaderSelectors.LOGO_BUTTON)

    def navigate_to_settings(self):
        self.page.click(HeaderSelectors.PROFILE_BUTTON)
        self.page.get_by_text(HeaderSelectors.SETTINGS_BUTTON).click()
    
    def navigate_to_magazine(self):
        self.page.click(HeaderSelectors.MAGAZINE_BUTTON)
    
    def navigate_to_support(self):
        self.page.click(HeaderSelectors.SUPPORT_BUTTON)
    
    def navigate_to_hotels(self):
        self.page.get_by_role('link', name=HeaderSelectors.HOTELS_BUTTON).click()

    def navigate_to_guides(self):
        self.page.get_by_role('link', name=HeaderSelectors.GUIDES_BUTTON).click()

    def navigate_to_favorites(self):
        self.page.get_by_role('link', name=HeaderSelectors.FAVORITES_BUTTON).click

    def navigate_to_b2b(self):
        self.page.get_by_role('link', name=HeaderSelectors.B2B_BUTTON).click()

    def change_origin_destination(self):   
        self.page.locator(HeaderSelectors.CHANGE_OF_DIRECTIONS_BUTTON).click()

    def fill_origin(self, city: str):
        self.page.locator(HeaderSelectors.ORIGIN_INPUT).click()
        self.page.locator(HeaderSelectors.ORIGIN_INPUT).fill(city)

    def fill_destination(self, city: str):
        self.page.locator(HeaderSelectors.DESTINATION_INPUT).click()
        self.page.locator(HeaderSelectors.DESTINATION_INPUT).fill(city)

    def select_start_date(self, start_date: str):
        self.page.locator(HeaderSelectors.START_DATE_FIELD).click()
        self.page.locator(f'[data-test-id="date-{start_date}"]').click()

    def select_end_date(self, end_date: str):
        self.page.locator(HeaderSelectors.END_DATE_FIELD).click()
        self.page.locator(f'[data-test-id="date-{end_date}"]').click()

    def click_button_search(self):
        self.page.locator(HeaderSelectors.SEARCH_BUTTON).click()

    def set_text_field_value_by_id(self, data_test_id: str, value: str):
        origin = self.page.locator(self.base_locator+'//[data-test-id="'+data_test_id+'"]")+""]')
        origin.click()
        origin.fill(value)

    def set_text_field_value_by_class(self, class_name: str, value: str):
        origin = self.page.locator('[contains(@class, "'+class_name+'")]')
        origin.click()
        origin.fill(value)