from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_GOOGLE_SEARCH = "//html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def get_text_from_google_search_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_GOOGLE_SEARCH).get_attribute('value')