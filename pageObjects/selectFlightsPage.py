from selenium.webdriver.common.by import By

from pageObjects.personalDetailsPage import PersonnalDetailsPage


class SelectFlightsPage:
    def __init__(self, driver):
        self.driver = driver
        self.flightTable = (By.CSS_SELECTOR, "table.table tbody tr")
        self.airlineName = (By.XPATH, "./td[3]")
        self.chooseFlightBtn = (By.CSS_SELECTOR, "input[type='submit']")


    def selectflight(self,airline):
        rows = self.driver.find_elements(*self.flightTable)
        for row in rows:
            displayedAirline = row.find_element(*self.airlineName).text
            if displayedAirline == airline:
                row.find_element(*self.chooseFlightBtn).click()
                break
        personnaldetailspage = PersonnalDetailsPage(self.driver)
        return personnaldetailspage