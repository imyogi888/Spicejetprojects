from selenium.webdriver.common.by import By


class flightbooking:

    def __init__(self,driver):
        self.driver= driver

    rntrip= (By.XPATH, "//div[text()='round trip']")
    frm= (By.XPATH, "//*[@id='main-container']/div/div[1]/div[3]/div[2]/div[3]/div/div[1]/div/div[2]/input")
    dest= (By.XPATH, "//*[@id='main-container']/div/div[1]/div[3]/div[2]/div[3]/div/div[3]/div[1]/div[2]/input")
    dpdate= (By.XPATH, "//div[@data-testid='undefined-month-March-2024']/div[3]/div[2]/div")
    rtdate= (By.XPATH, "//div[@data-testid='undefined-month-April-2024']/div[3]/div[2]/div")
    psg= (By.XPATH, "//div[@data-testid='home-page-travellers']")
    adtpsg= (By.XPATH, "//div[@data-testid='Adult-testID-plus-one-cta']")
    chdpsg= (By.XPATH, "//div[@data-testid='Children-testID-plus-one-cta']")
    dnecta= (By.XPATH, "//div[@data-testid='home-page-travellers-done-cta']")
    curncyclk= (By.XPATH, "//*[@id='main-container']/div/div[1]/div[3]/div[2]/div[5]/div[2]/div")
    crclst= (By.XPATH,"//div[@class='css-1dbjc4n r-14lw9ot r-z2wwpe r-1rjd0u6 r-1g94qm0 r-h3f8nf r-u8s1d r-8fdsdq']/div[2]/div/div")
    rdbtn= (By.XPATH, "//div[text()='Family & Friends']")
    srhflight= (By.XPATH, "//div[@data-testid='home-page-flight-cta']")
    ckbox= (By.CSS_SELECTOR, "svg[color$='#dddddd']")
    cntbtn= (By.CSS_SELECTOR,".css-1dbjc4n.r-1awozwy.r-z2wwpe.r-18u37iz.r-1777fci.r-d9fdf6.r-1w50u8q.r-ah5dr5")
    sgnup= (By.XPATH, "//div[text()='Signup']")


    def roundtrip(self):
        return self.driver.find_element(*flightbooking.rntrip)

    def initialpoint(self):
        return self.driver.find_element(*flightbooking.frm)

    def destination(self):
        return self.driver.find_element(*flightbooking.dest)

    def departuredate(self):
        return self.driver.find_elements(*flightbooking.dpdate)

    def returndate(self):
        return self.driver.find_elements(*flightbooking.rtdate)

    def passenderdrpdown(self):
        return self.driver.find_element(*flightbooking.psg)

    def adultpassengers(self):
        return self.driver.find_element(*flightbooking.adtpsg)

    def childpassengers(self):
        return self.driver.find_element(*flightbooking.chdpsg)

    def donecta(self):
        return self.driver.find_element(*flightbooking.dnecta)

    def currency(self):
        return self.driver.find_element(*flightbooking.curncyclk)

    def currencylist(self):
        return self.driver.find_elements(*flightbooking.crclst)

    def passengertype(self):
        return self.driver.find_element(*flightbooking.rdbtn)

    def searchflight(self):
        return self.driver.find_element(*flightbooking.srhflight)

    def popupclick(self):
        return self.driver.find_element(*flightbooking.ckbox)

    def continuebutton(self):
        return self.driver.find_element(*flightbooking.cntbtn)

    def signup(self):
        return self.driver.find_element(*flightbooking.sgnup)



















