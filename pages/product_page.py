from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import math
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Button 'Add to basket' is not present"

    def add_item_to_cart(self):
        self.should_be_add_to_cart_button()
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def should_be_messages(self):
        self.should_be_success_add_to_cart_message()
        self.should_be_correct_added_item_name()
        self.should_be_success_cart_total_message()
        self.should_be_correct_cart_total()

    def should_be_success_add_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_SUCCESS_ITEM), "Item added to cart message is not present"

    def should_be_correct_added_item_name(self):
        added_name = self.browser.find_element(*ProductPageLocators.ADD_SUCCESS_ITEM_NAME).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert added_name == item_name, "Item name in success message is different"

    def should_be_success_cart_total_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_SUCCESS_CART), "Cart total message is not present"

    def should_be_correct_cart_total(self):
        cart_total = self.browser.find_element(*ProductPageLocators.ADD_SUCCESS_CART_TOTAL).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert cart_total == item_price, "Cart total is different from item price"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
