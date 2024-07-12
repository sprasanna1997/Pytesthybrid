from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from Utility.Readdata import Readdata
from Utility.Logging import LogGen

#XPATHS

#----------------PracticeForm---------------------------
name_input_xpath='//input[@id="name"]'
email_input_xpath='//input[@id="email"]'
gender_rbtn_xpath='//input[@id="gender"]'
mobile_input_xpath='//input[@id="mobile"]'
dob_input_xpath='//input[@id="dob"]'
subject_input_xpath='//input[@id="subjects"]'
hobbies_cbox_xpath='//input[@id="hobbies"]'
picture_input_xpath='//input[@id="picture"]'
address_textarea_xpath='//textarea[@id="picture"]'
state_drpdwn_xpath='//select[@id="state"]'
city_drpdwn_xpath='//select[@id="city"]'
login_btn_xpath='//*[@type="submit"]'


#---------------Login & Register--------------------------------------
login1_btn_xpath='//a[text()=" Login"]'
newuser_btn_xpath='//a[text()="New User"]'
username_input_xpath='//*[@id="email"]'
password_input_xpath='//*[@id="password"]'

firstname_input_xpath='//input[@id="firstname"]'
lastname_input_xpath='//input[@id="lastname"]'
username1_input_xpath='//*[@id="username"]'
register_btn_xpath='//input[@value="Register"]'
forms_btn_xpath='//button[text()=" Forms"]'
login2_btn_xpath='//input[@value="Login"]'

class Forms:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
        self.logger=LogGen.loggen()

    def practice_form(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH,name_input_xpath))).send_keys(Readdata.username())
        self.wait.until(ec.presence_of_element_located((By.XPATH, email_input_xpath))).send_keys(Readdata.email())
        self.wait.until(ec.presence_of_element_located((By.XPATH, gender_rbtn_xpath))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, mobile_input_xpath))).send_keys(Readdata.mobileno())
        self.wait.until(ec.presence_of_element_located((By.XPATH, dob_input_xpath))).send_keys(Readdata.dob())
        self.wait.until(ec.presence_of_element_located((By.XPATH,subject_input_xpath))).send_keys(Readdata.subject())
        self.wait.until(ec.presence_of_element_located((By.XPATH, hobbies_cbox_xpath))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, picture_input_xpath))).send_keys(r'C://Users//chiya//Downloads//sampleFile.jpeg')
        self.wait.until(ec.presence_of_element_located((By.XPATH, address_textarea_xpath))).send_keys(Readdata.currentaddress())
        element=self.driver.find_element(By.XPATH,state_drpdwn_xpath)
        drp=Select(element)
        drp.select_by_index(1)
        element = self.driver.find_element(By.XPATH, city_drpdwn_xpath)
        drp = Select(element)
        drp.select_by_value("Agra")
        #self.wait.until(ec.element_to_be_clickable((By.XPATH, login_btn_xpath))).click()
        self.logger.info('******TC010-Forms -Practice Form- Passed*******')


    def login_and_register(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH,login1_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH,newuser_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, firstname_input_xpath))).send_keys(Readdata.username())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lastname_input_xpath))).send_keys(Readdata.lastname())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, username1_input_xpath))).send_keys(Readdata.email())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, password_input_xpath))).send_keys(Readdata.password())
        self.wait.until(ec.element_to_be_clickable((By.XPATH,register_btn_xpath))).click()
        self.logger.info('******TC011-Forms -Form Register- Passed*******')
        self.wait.until(ec.element_to_be_clickable((By.XPATH, forms_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, login1_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, username_input_xpath))).send_keys(Readdata.email())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, password_input_xpath))).send_keys(Readdata.password())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, login2_btn_xpath))).click()
        self.logger.info('******TC012-Forms -Form Login- Passed*******')









