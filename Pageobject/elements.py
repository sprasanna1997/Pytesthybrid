import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from Utility.Readdata import Readdata
from Utility.Logging import LogGen

#XPATHS

#---------------Text Box---------------------
elements_btn_xpath = '//*[text()=" Elements"]'
textbox_btn_xpath='//*[text()=" Text Box"]'
fullname_input_xpath='//input[@id="fullname"]'
email_input_xpath='//input[@id="email"]'
address_textarea_xpath='//textarea[@id="address"]'
password_input_xpath='//input[@id="password"]'
submit_btn_xpath='//input[@type="submit"]'


#---------------Checkbox Box---------------------
checkbox_btn_xpath='//*[text()=" Check Box"]'
mainlvl1_checkbox_xpath='(//*[@class="plus"])[1]'
sublvl1_checkbox_xpath='(//*[@class="plus"])[1]'
lastlvl1_checkbox_xpath='//*[@id="c_io_1"]'
lastlvl6_checkbox_xpath='//*[@id="c_io_6"]'
clsmainlvl1_checkbox_xpath='(//span[@class="plus minus"])[1]'
mainlvl2_checkbox_xpath='(//span[@class="plus"])[2]'
sublvl3_checkbox_xpath='(//*[@class="plus"])[2]'
lastlvl11_checkbox_xpath='//*[@id="c_io_11"]'
sublvl4_checkbox_xpath='(//*[@class="plus"])[2]'
lastlvl16_checkbox_xpath='//*[@id="c_io_16"]'
clsmainlvl2_checkbox_xpath='(//span[@class="plus minus"])[3]'
clssublvl2_checkbox_xpath='(//*[@class="plus minus"])[4]'

#------------------Radio Button--------------------
radio_rbtn_xpath='//*[text()=" Radio Button"]'
yes_rbtn_xpath='//*[@value="igottwo"]'
getyes_text_xpath='//*[@id="check"]'
impressive_rbtn_xpath='//*[@value="igotthree"]'
getimp_text_xpath='//*[@id="check1"]'
no_rbtn_xpath='//*[@value="option3"]'


#----------------Web Tables-------------------------
webtables_btn_xpath='//*[text()=" Web Tables"]'
add_btn_xpath='//button[text()="Add"]'
delete_btn_xpath='(//td[text()="Kierra"] /..//a[@title="delete"])[1]'
edit_btn_xpath='(//td[text()="Kierra"] /..//a[@title="edit"])[1]'
fname_input_xpath='(//input[@id="firstname"])[1]'
lname_input_xpath='(//input[@id="lastname"])[1]'
email1_input_xpath='(//input[@id="email"])[1]'
age_input_xpath='(//input[@id="age"])[1]'
salary_input_xpath='(//input[@id="salary"])[1]'
department_input_xpath='(//input[@id="deparment"])[1]'
submit1_btn_xpath='(//input[@type="submit"])[1]'
row_table_xpath='//tr'
search_input_xpath='//*[@placeholder="Type to Search"]'
search_btn_xpath='//button[@class="btn btn-outline-secondary"]'
efname_input_xpath='(//input[@id="firstname"])[2]'
elname_input_xpath='(//input[@id="lastname"])[2]'
eemail1_input_xpath='(//input[@id="email"])[2]'
esubmit1_btn_xpath='(//input[@type="submit"])[2]'

class Elements:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.loggers=LogGen.loggen()
    def click_element(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, elements_btn_xpath))).click()

    def textbox(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, textbox_btn_xpath))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, fullname_input_xpath))).send_keys(Readdata.username())
        self.wait.until(ec.presence_of_element_located((By.XPATH, email_input_xpath))).send_keys(Readdata.email())
        self.wait.until(ec.presence_of_element_located((By.XPATH, address_textarea_xpath))).send_keys(Readdata.currentaddress())
        self.wait.until(ec.presence_of_element_located((By.XPATH, password_input_xpath))).send_keys(Readdata.password())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, submit_btn_xpath))).click()
        self.loggers.info("******TC001-Elements -TextBox -Submission Passed*******")
        self.driver.quit()

    def checkbox_mainlevel1(self):
        self.click_element()
        self.wait.until(ec.element_to_be_clickable((By.XPATH,checkbox_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, mainlvl1_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, sublvl1_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lastlvl1_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, mainlvl1_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lastlvl6_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, clsmainlvl1_checkbox_xpath))).click()
        self.loggers.info("******TC002.1-Elements -CheckBox -Mainlevel1 Passed*******")

    def checkbox_mainlevel2(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, mainlvl2_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, sublvl3_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lastlvl11_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, sublvl4_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH,clssublvl2_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lastlvl16_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, clsmainlvl2_checkbox_xpath))).click()
        self.loggers.info("******TC002.2-Elements -CheckBox -Mainlevel2 Passed*******")
        self.driver.quit()

    def radiobutton_yes(self):
        self.click_element()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, radio_rbtn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, yes_rbtn_xpath))).click()
        actual_value=self.driver.find_element(By.XPATH,getyes_text_xpath).text
        assert actual_value=="You have checked Yes","Wrong value in the Get text"
        self.loggers.info("******TC003.1-Elements -Radio Button -Yes - Passed*******")


    def radiobutton_impressive(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, impressive_rbtn_xpath))).click()
        actual_value = self.driver.find_element(By.XPATH, getimp_text_xpath).text
        assert actual_value == "You have checked Impressive", "Wrong value in the Get text"
        self.loggers.info("******TC003.2-Elements -Radio Button -Impressive - Passed*******")

    def radiobutton_enable_check(self):
        enabled=self.driver.find_element(By.XPATH,no_rbtn_xpath).is_enabled()
        assert enabled==False,"Radio Button No is disabled but got Wrong value from the response"
        self.loggers.info("******TC003.3-Elements -Radio Button -Disable Check - Passed*******")
        self.driver.quit()

    def webtables_add_user(self):
        self.click_element()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, webtables_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, add_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, fname_input_xpath))).send_keys(Readdata.username())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lname_input_xpath))).send_keys(Readdata.lastname())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, email1_input_xpath))).send_keys(Readdata.email())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, age_input_xpath))).send_keys(Readdata.age())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, salary_input_xpath))).send_keys(Readdata.salary())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, department_input_xpath))).send_keys(Readdata.department())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, submit1_btn_xpath))).click()
        self.loggers.info("******TC004.1-Elements -WebTables -Register New User - Passed*******")

    def webtables_delete_user(self):
        table_row=len(self.driver.find_elements(By.XPATH,row_table_xpath))
        print(table_row)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, delete_btn_xpath))).click()
        table_row2 = len(self.driver.find_elements(By.XPATH, row_table_xpath))
        assert table_row2==table_row-1,"Row deletion failed"
        self.loggers.info("******TC004.2-Elements -WebTables -Delete the User - Passed*******")
    def webtables_edit_user(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, edit_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, efname_input_xpath))).send_keys(Readdata.username())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, elname_input_xpath))).send_keys(Readdata.lastname())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, eemail1_input_xpath))).send_keys(Readdata.email())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, esubmit1_btn_xpath))).click()
        self.loggers.info("******TC004.1-Elements -WebTables -Edit the User - Passed*******")

    def webtables_search_user(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, search_input_xpath))).send_keys(Readdata.username())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, search_btn_xpath))).click()
        self.loggers.info("******TC004.1-Elements -WebTables -Search the User - Passed*******")
        self.driver.quit()
