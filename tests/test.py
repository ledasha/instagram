import time

from selenium import webdriver


from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_result import SearchResultPage

driver = webdriver.Chrome('C:\\temp\chromedriver_win32\\chromedriver.exe')
driver.implicitly_wait(5)
driver.get("https://www.instagram.com/accounts/login/")

login_page = LoginPage(driver)
login_page.enter_username("patyuryy")
login_page.enter_password("Taburetka133")
login_page.click_login()

main_page = MainPage(driver)
main_page.click_not_now_button()
main_page.type_in_search_field("fitness")
main_page.click_result_with_text("#fitness")

search_page = SearchResultPage(driver)
time.sleep(5)
assert "Follow" in search_page.get_follow_button_text()

driver.quit()
