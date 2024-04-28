from base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):

    def search_text_title(self):
        search_title = self.find_element(MainPageLocators.LOCATOR_MAIN_PAGE_TITLE)
        title_text = search_title.text
        return title_text
    

