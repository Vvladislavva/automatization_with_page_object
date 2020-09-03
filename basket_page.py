from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Busket is not empty, but should be"

    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_IN_EMPTY_BASKET), \
            "Message that the basket is empty is not presented"
