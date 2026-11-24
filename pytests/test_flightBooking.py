import json
import pytest

from pageObjects.searchFlightsPage import SearchFlightsPage
test_data_path='../data/flightBookingData.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_flightBookingMain(browserInstance, test_list_item):
    driver = browserInstance
    searchflightspage = SearchFlightsPage(driver)
    selectflightspage= searchflightspage.searchflights(test_list_item["fromPlace"],test_list_item["toPlace"])
    personnaldetailspage = selectflightspage.selectflight(test_list_item["airline"])
    flightMessage= personnaldetailspage.airlineNameCheck()
    assert flightMessage == "Your flight from TLV to SFO has been reserved."
    personnaldetailspage.personnalDetails(test_list_item["name"],test_list_item["address"],
                test_list_item["city"],test_list_item["state"],test_list_item["postalcode"])
    bookingconfirmationpage= personnaldetailspage.cardDetails(test_list_item["name"],
                test_list_item["cardType"],test_list_item["cardNum"])
    message = bookingconfirmationpage.confirmationMessage()
    assert message == "Thank you for your purchase today!"


