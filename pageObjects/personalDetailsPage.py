from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.bookingConfirmationPage import BookingConfirmationPage


class PersonnalDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.flightMessage = (By.TAG_NAME, "h2")
        self.name = (By.ID, "inputName")
        self.address = (By.ID, "address")
        self.city = (By.ID, "city")
        self.state = (By.ID, "state")
        self.postalCode = (By.ID, "zipCode")
        self.CardType = (By.ID, "cardType")
        self.creditcardNum = (By.ID, "creditCardNumber")
        self.nameOnCard = (By.ID, "nameOnCard")
        self.SubmitBtn = (By.CSS_SELECTOR, "input[type='submit']")


    def airlineNameCheck(self):
        flightMessage = self.driver.find_element(*self.flightMessage).text
        return flightMessage


    def personnalDetails(self, name, address, city, state, postalcode):
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.address).send_keys(address)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.state).send_keys(state)
        self.driver.find_element(*self.postalCode).send_keys(postalcode)


    def cardDetails(self, name, cardType, cardNum):
        self.driver.find_element(*self.CardType).click()
        cardTypeDropdown = Select(self.driver.find_element(*self.CardType))
        cardTypeDropdown.select_by_value(cardType)
        self.driver.find_element(*self.creditcardNum).send_keys(cardNum)
        self.driver.find_element(*self.nameOnCard).send_keys(name)
        self.driver.find_element(*self.SubmitBtn).click()
        bookingconfirmationpage = BookingConfirmationPage(self.driver)
        return bookingconfirmationpage


