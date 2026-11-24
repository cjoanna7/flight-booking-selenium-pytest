from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.selectFlightsPage import SelectFlightsPage


class SearchFlightsPage:
    def __init__(self, driver):
        self.driver = driver
        self.fromPort = (By.CSS_SELECTOR, "select[name='fromPort']")
        self.toPort= (By.CSS_SELECTOR, "select[name='toPort']")
        self.searchBtn = (By.CSS_SELECTOR, "input[type='submit']")

    def searchflights(self, fromPlace, toPlace):
        self.driver.find_element(*self.fromPort).click()
        departureDropdown = Select(self.driver.find_element(*self.fromPort))
        departureDropdown.select_by_value(fromPlace)
        self.driver.find_element(*self.toPort).click()
        arrivalDropdown = Select(self.driver.find_element(*self.toPort))
        arrivalDropdown.select_by_value(toPlace)
        self.driver.find_element(*self.searchBtn).click()
        selectflightspage = SelectFlightsPage(self.driver)
        return selectflightspage