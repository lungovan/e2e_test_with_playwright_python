from playwright.sync_api import expect
from tests.pages.page_objects.home_page import HomePage


# def test_home_page_title(browser_context, home_page, logger):
#     home_page.load()
#     expect(home_page.page).to_have_title(HomePage.PAGE_TITLE)
#     logger.logger.info("PAGE_TITLE=" + str(home_page.page.title()))
