from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOCATOR_INPUT_LOGIN = (By.XPATH, '//input[@id="user-name"]')
    LOCATOR_INPUT_PASSWORD = (By.XPATH, '//input[@id="password"]')
    LOCATOR_LOGIN_BUTTON = (By.XPATH, '//input[@id="login-button"]')

class MainPageLocators:
    LOCATOR_MAIN_PAGE_TITLE = (By.XPATH, '//div[@class="app_logo"]')


