from selenium.webdriver.common.by import By


class BookingConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.displayedMessage = (By.TAG_NAME, "h1")


    def confirmationMessage(self):
        message = self.driver.find_element(*self.displayedMessage).text
        return message