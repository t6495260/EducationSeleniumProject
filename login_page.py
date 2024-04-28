from base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_login(self, word):
        input_login = self.find_element(LoginPageLocators.LOCATOR_INPUT_LOGIN)
        input_login.send_keys(word)
        print('Login OK')
        return input_login

    def enter_password(self, word):
        input_password = self.find_element(LoginPageLocators.LOCATOR_INPUT_PASSWORD)
        input_password.send_keys(word)
        print('Password OK')
        return input_password

    def press_login_button(self):
        press_button = self.find_element(LoginPageLocators.LOCATOR_LOGIN_BUTTON)
        press_button.click()
        print('Login button OK')
        return press_button
    
    








# class AutorizationMethod(BasePage):
    
#     def autorization(self):
        
