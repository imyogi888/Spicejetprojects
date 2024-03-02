import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Testdata.Signuppagedata import signuppagedata
from pageobjects.Registration import registerpage
from pageobjects.flightbooking import flightbooking
from utilities.baseclass import Testone


class TestSignup(Testone):

    def test_signup(self,getdata):
        flight= flightbooking(self.driver)
        flight.signup().click()
        self.windowhandle()

        register= registerpage(self.driver)
        self.gender(register.genders(),getdata["Gender"])

        register.firstname().send_keys(getdata["firstname"])

        register.lastname().send_keys(getdata["lastname"])

        self.country(register.countries(),getdata["country"])

        register.dateofbirth().click()

        self.month(register.months(),getdata["month"])

        self.year(register.years(),getdata["year"])

        dates = register.date1()

        for date in dates:
            if date.text == getdata["date"]:
                date.click()
                break

        register.phonenumber().send_keys(getdata["phonenumber"])
        register.gmaiid().send_keys(getdata["gmailid"])
        register.newpassword().send_keys(getdata["newpassword"])
        register.confirmpassword().send_keys(getdata["confirmpassword"])
        time.sleep(7)
        wait= WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='defaultCheck1']")))
        register.checkboxes().click()
        self.driver.find_element(By.CSS_SELECTOR,"button[type='button']").click()

    @pytest.fixture(params= signuppagedata.test_signuppage_data)
    def getdata(self,request):
        return request.param







