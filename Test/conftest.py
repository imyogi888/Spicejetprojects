import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("C:\\mybrowserdriver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()
    request.cls.driver= driver
    yield
    driver.quit()



