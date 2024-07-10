import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from Utility.Readdata import Readdata
from Utility.Logging import LogGen

#XPATH

elements_btn_xpath = '//*[text()=" Elements"]'
textbox_btn_xpath='//*[text()=" Text Box"]'
fullname_input_xpath='//input[@id="fullname"]'
email_input_xpath='//input[@id="email"]'
address_textarea_xpath='//textarea[@id="address"]'
password_input_xpath='//input[@id="password"]'
submit_btn_xpath='//input[@type="submit"]'

checkbox_btn_xpath='//*[text()=" Check Box"]'
mainlvl1_checkbox_xpath='(//*[@class="plus"])[1]'
sublvl1_checkbox_xpath='(//*[@class="plus"])[1]'
    #'(//*[@class="plus minus"])[2]'
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

    def checkbox(self):
        self.click_element()
        self.wait.until(ec.element_to_be_clickable((By.XPATH,checkbox_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, mainlvl1_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, sublvl1_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lastlvl1_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, mainlvl1_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lastlvl6_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, clsmainlvl1_checkbox_xpath))).click()
        self.loggers.info("******TC002.1-Elements -CheckBox -Mainlevel1 Passed*******")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, mainlvl2_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, sublvl3_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lastlvl11_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, sublvl4_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH,clssublvl2_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lastlvl16_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, clsmainlvl2_checkbox_xpath))).click()
        self.loggers.info("******TC002.2-Elements -CheckBox -Mainlevel2 Passed*******")
        self.driver.quit()

