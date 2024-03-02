from selenium.webdriver.common.by import By


class registerpage:

    def __init__(self,driver):
        self.driver= driver


    gndr= (By.XPATH, "//select[@class='form-control form-select ']")
    fstnme= (By.ID, "first_name")
    lstnme= (By.ID, "last_name")
    cntry= (By.XPATH, "//select[@class='form-control form-select']")
    dob= (By.ID, "dobDate")
    mnth= (By.XPATH, "//select[@class='react-datepicker__month-select']")
    yr= (By.XPATH, "//select[@class='react-datepicker__year-select']")
    dts= (By.XPATH, "//div[@class='react-datepicker__month']/div/div")
    phnm= (By.XPATH, "//input[@type='tel']")
    gml= (By.XPATH, "//*[@id='email_id']")
    npsswrd= (By.ID, "new-password")
    cpsswrd= (By.ID, "c-password")
    chcbx= (By.XPATH, "//*[@id='defaultCheck1']")

    def genders(self):
        return self.driver.find_element(*registerpage.gndr)

    def firstname(self):
        return self.driver.find_element(*registerpage.fstnme)

    def lastname(self):
        return self.driver.find_element(*registerpage.lstnme)

    def countries(self):
        return self.driver.find_element(*registerpage.cntry)

    def dateofbirth(self):
        return self.driver.find_element(*registerpage.dob)

    def months(self):
        return self.driver.find_element(*registerpage.mnth)

    def years(self):
        return self.driver.find_element(*registerpage.yr)

    def date1(self):
        return self.driver.find_elements(*registerpage.dts)

    def phonenumber(self):
        return self.driver.find_element(*registerpage.phnm)

    def gmaiid(self):
        return self.driver.find_element(*registerpage.gml)

    def newpassword(self):
        return self.driver.find_element(*registerpage.npsswrd)

    def confirmpassword(self):
        return self.driver.find_element(*registerpage.cpsswrd)

    def checkboxes(self):
        return self.driver.find_element(*registerpage.chcbx)



