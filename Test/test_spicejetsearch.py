from selenium.webdriver.common.by import By
from pageobjects.flightbooking import flightbooking
from utilities.baseclass import Testone


class TestSearch(Testone):

    def test_spicejet(self):

        flights= flightbooking(self.driver)
        flights.roundtrip().click()
        flights.initialpoint().send_keys("agr")
        flights.destination().send_keys("del")
        dates = flights.departuredate()

        data = "10"

        for date in dates:
            if date.text == data:
                date.click()
                break

        dates2 = flights.returndate()

        data2 = "14"

        for datem in dates2:
            if datem.text == data2:
                datem.click()
                break

        flights.passenderdrpdown().click()

        for i in range(1, 3):
            flights.adultpassengers().click()
            break

        for i in range(1, 2):
            flights.childpassengers().click()
            break

        flights.donecta().click()
        flights.currency().click()

        currencies = flights.currencylist()

        for currency in currencies:
            if currency.text == "KWD":
                currency.click()
                break

        flights.passengertype().click()
        flights.searchflight().click()
        flights.popupclick().click()
        flights.continuebutton().click()


