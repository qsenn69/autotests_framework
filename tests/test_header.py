from playwright.sync_api import Page, expect
from utils.config import Config
from pages.header import Header
from utils.data import Data
    
def test_search(header: Header):
    start_form, end_form, start_url, end_url = Data.get_formatted_range(5, 12)
    header.fill_origin("Москва")
    header.fill_destination("Тайбей")
    header.select_start_date(start_form)
    header.select_end_date(end_form)
    header.click_button_search()
    header.assert_url(f"{Config.BASE_URL}?params=MOW{start_url}TPE{end_url}1&with_request=true")

def test_origin_valid_city(header: Header, page: Page):
    header.fill_origin("Москва")
    expect(page.locator('[data-test-id="origin-input"]')).to_have_value("Москва")

def test_destination_valid_city(header: Header, page: Page):
    header.fill_destination("Иркутск")
    expect(page.locator('[data-test-id="destination-input"]')).to_have_value("Иркутск")

def test_change_origin_destination(header: Header, page: Page):
    header.click(('[data-test-id="origin-input"]'))
    header.fill_origin("Москва")
    header.fill_destination("Фукуок")
    page.wait_for_timeout(2000)
    page.locator('text=Фукуок').filter(has_not=page.locator('[data-test-id="destination-input"]')).first.click()
    header.change_origin_destination()
    expect(page.locator('[data-test-id="origin-input"]')).to_have_value("Фукуок")
    expect(page.locator('[data-test-id="destination-input"]')).to_have_value("Москва")

def test_origin_invalid_city(header: Header, page: Page):
    header.fill_origin("Ксилоран")
    expect(page.locator('[data-test-id="origin-input"]')).to_have_value("Ксилоран")
    expect(page.locator('[data-test-id="status-message"]')).to_be_visible()

def test_check_calendar_open(header: Header, page: Page):  
    header.page.locator('[data-test-id="start-date-field"]').click()
    expect(page.locator('[data-test-id="dropdown"]')).to_be_visible()

def test_open_settings(header: Header, page: Page): 
    header.navigate_to_settings()
    header.assert_url(f"{Config.BASE_URL}my/settings")

def test_fill_code_IATA(header: Header, page: Page):
    header.fill_origin("MSQ")
    expect(page.locator('[data-test-id="origin-input"]')).to_have_value("MSQ")