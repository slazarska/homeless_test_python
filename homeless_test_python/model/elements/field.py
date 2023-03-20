from selene import have


class Field:

    def __init__(self, element):
        self.element = element

    def input_value(self, test_data='text'):
        self.element.set_value(test_data).press_tab()
        self.element.should(have.value(test_data))


#def input_value(selector, test_data='text'):
#  browser.element(selector).set_value(test_data).press_tab()
#  browser.element(selector).should(have.value(test_data))
