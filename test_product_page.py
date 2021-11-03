from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_messages()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    assert page.is_not_element_present(*ProductPageLocators.ADD_SUCCESS_ITEM), "Item added to cart message is not present, but should be"

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.ADD_SUCCESS_ITEM), "Item added to cart message is present, but shouldn't"
    
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    assert page.is_disappeared(*ProductPageLocators.ADD_SUCCESS_ITEM), "Item added to cart message disappeared, but shouldn't"

def test_guest_should_see_basket_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(*self.page.generate_user_data())
        self.page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.ADD_SUCCESS_ITEM), "Item added to cart message is present, but shouldn't"

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_cart()
        page.should_be_messages()
