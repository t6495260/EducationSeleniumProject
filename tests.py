from login_page import LoginPage
from main_page import MainPage
import pytest

users = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
password = 'secret_sauce'


def autorization(browser, login):
    autorization = LoginPage(browser)
    autorization.go_to_site()
    autorization.enter_login(login)
    autorization.enter_password(password)
    autorization.press_login_button()

@pytest.mark.parametrize('login', users)
def test_main_page(browser, login):
    autorization(browser, login)
    title = MainPage(browser)
    title_text = title.search_text_title()
    assert title_text == 'Swag Labs', 'Заголовок страницы не соответствует'
    print('Заголовок страницы ОК')













# @pytest.mark.parametrize('login', users)
# def test_autorization(browser, login):
#     autorization = LoginPage(browser)
#     autorization.go_to_site()
#     autorization.enter_login(login)
#     autorization.enter_password(password)
#     autorization.press_login_button()

# def test_main_page(browser):
#     title = MainPage(browser)
#     title_text = title.search_text_title()
#     assert title_text == 'Swag Labs'