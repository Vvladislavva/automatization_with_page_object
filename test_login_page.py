from .pages.login_page import LoginPage
link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_can_go_to_login_url(browser):
    url = LoginPage(browser, link)
    url.open()
    url.should_be_login_url()


def test_guest_should_see_login_form(browser):
    form = LoginPage(browser, link)
    form.open()
    form.should_be_login_form()


def test_guest_should_see_register_form(browser):
    reg_form = LoginPage(browser, link)
    reg_form.open()
    reg_form.should_be_register_form()
