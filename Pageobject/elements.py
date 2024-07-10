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



class Elements:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.loggers=LogGen.loggen()
    def click_element(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, elements_btn_xpath))).click()

    def filling_checkbox(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, textbox_btn_xpath))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, fullname_input_xpath))).send_keys(Readdata.username())
        self.wait.until(ec.presence_of_element_located((By.XPATH, email_input_xpath))).send_keys(Readdata.email())
        self.wait.until(ec.presence_of_element_located((By.XPATH, address_textarea_xpath))).send_keys(Readdata.currentaddress())
        self.wait.until(ec.presence_of_element_located((By.XPATH, password_input_xpath))).send_keys(Readdata.password())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, submit_btn_xpath))).click()
        self.loggers.info("******TC001-Elements -TextBox -Submission Passed*******")
        self.driver.quit()
