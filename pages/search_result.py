from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultPage(BasePage):

    BUTTON_FOLLOW = (By.XPATH, "//*[@id='react-root']/section/main/header/div[2]/div/button")

    def _verify_page(self):
        self.on_this_page(self.BUTTON_FOLLOW)

    def get_follow_button_text(self):
        return self.get_text(self.BUTTON_FOLLOW, "Follow")
