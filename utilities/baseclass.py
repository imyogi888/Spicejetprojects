import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class Testone:

    def windowhandle(self):
        windowsopened = self.driver.window_handles
        self.driver.switch_to.window(windowsopened[1])

    def gender(self,locator,text):
        gender = Select(locator)
        gender.select_by_visible_text(text)

    def country(self,locator,text):
        country = Select(locator)
        country.select_by_visible_text(text)

    def month(self,locator,text):
        month = Select(locator)
        month.select_by_visible_text(text)

    def year(self,locator,text):
        year = Select(locator)
        year.select_by_visible_text(text)

