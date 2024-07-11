import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
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
textbox_btn_xpath = '//*[text()=" Text Box"]'
fullname_input_xpath = '//input[@id="fullname"]'
email_input_xpath = '//input[@id="email"]'
address_textarea_xpath = '//textarea[@id="address"]'
password_input_xpath = '//input[@id="password"]'
submit_btn_xpath = '//input[@type="submit"]'

#---------------Checkbox Box---------------------
checkbox_btn_xpath = '//*[text()=" Check Box"]'
mainlvl1_checkbox_xpath = '(//*[@class="plus"])[1]'
sublvl1_checkbox_xpath = '(//*[@class="plus"])[1]'
lastlvl1_checkbox_xpath = '//*[@id="c_io_1"]'
lastlvl6_checkbox_xpath = '//*[@id="c_io_6"]'
clsmainlvl1_checkbox_xpath = '(//span[@class="plus minus"])[1]'
mainlvl2_checkbox_xpath = '(//span[@class="plus"])[2]'
sublvl3_checkbox_xpath = '(//*[@class="plus"])[2]'
lastlvl11_checkbox_xpath = '//*[@id="c_io_11"]'
sublvl4_checkbox_xpath = '(//*[@class="plus"])[2]'
lastlvl16_checkbox_xpath = '//*[@id="c_io_16"]'
clsmainlvl2_checkbox_xpath = '(//span[@class="plus minus"])[3]'
clssublvl2_checkbox_xpath = '(//*[@class="plus minus"])[4]'

#------------------Radio Button--------------------
radio_rbtn_xpath = '//*[text()=" Radio Button"]'
yes_rbtn_xpath = '//*[@value="igottwo"]'
getyes_text_xpath = '//*[@id="check"]'
impressive_rbtn_xpath = '//*[@value="igotthree"]'
getimp_text_xpath = '//*[@id="check1"]'
no_rbtn_xpath = '//*[@value="option3"]'

#----------------Web Tables-------------------------
webtables_btn_xpath = '//*[text()=" Web Tables"]'
add_btn_xpath = '//button[text()="Add"]'
delete_btn_xpath = '(//td[text()="Kierra"] /..//a[@title="delete"])[1]'
edit_btn_xpath = '(//td[text()="Kierra"] /..//a[@title="edit"])[1]'
fname_input_xpath = '(//input[@id="firstname"])[1]'
lname_input_xpath = '(//input[@id="lastname"])[1]'
email1_input_xpath = '(//input[@id="email"])[1]'
age_input_xpath = '(//input[@id="age"])[1]'
salary_input_xpath = '(//input[@id="salary"])[1]'
department_input_xpath = '(//input[@id="deparment"])[1]'
submit1_btn_xpath = '(//input[@type="submit"])[1]'
row_table_xpath = '//tr'
search_input_xpath = '//*[@placeholder="Type to Search"]'
search_btn_xpath = '//button[@class="btn btn-outline-secondary"]'
efname_input_xpath = '(//input[@id="firstname"])[2]'
elname_input_xpath = '(//input[@id="lastname"])[2]'
eemail1_input_xpath = '(//input[@id="email"])[2]'
esubmit1_btn_xpath = '(//input[@type="submit"])[2]'

#-----------------Buttons------------------------
buttons_btn_xpath = '// *[text() = " Buttons"]'
clickme_btn_xpath = '//button[text()="Click Me"]'
rightclickme_btn_xpath = '//button[text()="Right Click Me"]'
doubleclickme_btn_xpath = '//button[text()="Double Click Me"]'
singleclick_txt_xpath = '//div[@id="welcomeDiv"]'
doubleclick_txt_xpath = '//*[text()="You have Double clicked "]'

#---------------------Links----------------------------------------
links_btn_xpath = '//*[text()=" Links"]'
home_link_xpath = '//a[text()="Home"]'
homewPWPU_link_xpath = '//a[text()="HomewPWPU"]'
created_link_xpath = '//a[text()="Created"]'
nocontent_link_xpath = '//a[text()="No Content"]'
moved_link_xpath = '//a[text()="Moved"]'
badrequest_link_xpath = '//a[text()="Bad Request"]'
unauthorized_link_xpath = '//a[text()="Unauthorized"]'
forbidden_link_xpath = '//a[text()="Forbidden"]'
notfound_link_xpath = '//a[text()="Not Found"]'

create_txt_xpath = '//div[@class="create"]'
nocontent_txt_xpath = '//div[@class="nocontent"]'
move_txt_xpath = '//div[@class="move"]'
badrequest_txt_xpath = '//div[@class="brequest"]'
authorize_txt_xpath = '//div[@class="authorize"]'
bidden_txt_xpath = '//div[@class="bidden"]'
notfound_txt_xpath = '//div[@class="nfound"]'


class Elements:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.loggers = LogGen.loggen()

    def click_element(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, elements_btn_xpath))).click()

    def textbox(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, textbox_btn_xpath))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, fullname_input_xpath))).send_keys(Readdata.username())
        self.wait.until(ec.presence_of_element_located((By.XPATH, email_input_xpath))).send_keys(Readdata.email())
        self.wait.until(ec.presence_of_element_located((By.XPATH, address_textarea_xpath))).send_keys(
            Readdata.currentaddress())
        self.wait.until(ec.presence_of_element_located((By.XPATH, password_input_xpath))).send_keys(Readdata.password())
        self.wait.until(ec.element_to_be_clickable((By.XPATH, submit_btn_xpath))).click()
        self.loggers.info("******TC001-Elements -TextBox -Submission Passed*******")

    def checkbox_mainlevel1(self):
        self.click_element()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, checkbox_btn_xpath))).click()
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
        self.wait.until(ec.element_to_be_clickable((By.XPATH, clssublvl2_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, lastlvl16_checkbox_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, clsmainlvl2_checkbox_xpath))).click()
        self.loggers.info("******TC002.2-Elements -CheckBox -Mainlevel2 Passed*******")

    def radiobutton_yes(self):
        self.click_element()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, radio_rbtn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, yes_rbtn_xpath))).click()
        actual_value = self.driver.find_element(By.XPATH, getyes_text_xpath).text
        assert actual_value == "You have checked Yes", "Wrong value in the Get text"
        self.loggers.info("******TC003.1-Elements -Radio Button -Yes - Passed*******")

    def radiobutton_impressive(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, impressive_rbtn_xpath))).click()
        actual_value = self.driver.find_element(By.XPATH, getimp_text_xpath).text
        assert actual_value == "You have checked Impressive", "Wrong value in the Get text"
        self.loggers.info("******TC003.2-Elements -Radio Button -Impressive - Passed*******")

    def radiobutton_enable_check(self):
        enabled = self.driver.find_element(By.XPATH, no_rbtn_xpath).is_enabled()
        assert enabled == False, "Radio Button No is disabled but got Wrong value from the response"
        self.loggers.info("******TC003.3-Elements -Radio Button -Disable Check - Passed*******")

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
        table_row = len(self.driver.find_elements(By.XPATH, row_table_xpath))
        self.wait.until(ec.element_to_be_clickable((By.XPATH, delete_btn_xpath))).click()
        table_row2 = len(self.driver.find_elements(By.XPATH, row_table_xpath))
        assert table_row2 == table_row - 1, "Row deletion failed"
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

    def buttons_single_click(self):
        self.click_element()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, buttons_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, clickme_btn_xpath))).click()
        single_click_txt = self.driver.find_element(By.XPATH, singleclick_txt_xpath).text
        assert single_click_txt == "You have done a dynamic click", "Single click Text got from Web is wrong"
        self.loggers.info("******TC005.1-Elements -Buttons -Single Click - Passed*******")

    def buttons_right_click(self):
        actions = ActionChains(self.driver)
        actions.context_click(self.driver.find_element(By.XPATH, rightclickme_btn_xpath)).perform()
        self.loggers.info("******TC005.2-Elements -Buttons -Right Click - Passed*******")

    def buttons_double_click(self):
        actions = ActionChains(self.driver)
        actions.double_click(self.driver.find_element(By.XPATH, doubleclickme_btn_xpath)).perform()
        double_click_text = self.driver.find_element(By.XPATH, doubleclick_txt_xpath).text
        assert double_click_text == "You have Double clicked", "Double click Text got from Web is wrong"
        self.loggers.info("******TC005.3-Elements -Buttons -Double Click - Passed*******")

    def links_new_tab(self):
        self.click_element()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, links_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, home_link_xpath))).click()
        windows = self.driver.window_handles
        current_window = self.driver.current_window_handle
        for window in windows:
            self.driver.switch_to.window(window)
            if self.driver.title == "Quality Tutorials, Video Courses, and eBooks":
                self.driver.close()
                self.driver.switch_to.window(current_window)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, homewPWPU_link_xpath))).click()
        windows = self.driver.window_handles
        for window in windows:
            self.driver.switch_to.window(window)
            if self.driver.title != "Selenium Practice - Links":
                self.driver.close()
                self.driver.switch_to.window(current_window)

        self.loggers.info("******TC006.1-Elements -Links -New Tab - Passed*******")


    def links_existing_tab(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, created_link_xpath))).click()
        assert 'Link has responded with staus 201 and status text Created' == self.driver.find_element(By.XPATH,create_txt_xpath).text

        self.wait.until(ec.element_to_be_clickable((By.XPATH, nocontent_link_xpath))).click()
        assert 'Link has responded with staus 204 and status text No Content' == self.driver.find_element(By.XPATH,nocontent_txt_xpath).text

        self.wait.until(ec.element_to_be_clickable((By.XPATH, moved_link_xpath))).click()
        assert 'Link has responded with staus 301 and status text Moved Permanently' == self.driver.find_element(By.XPATH,move_txt_xpath).text

        self.wait.until(ec.element_to_be_clickable((By.XPATH, badrequest_link_xpath))).click()
        assert 'Link has responded with staus 400 and status text Bad Request' == self.driver.find_element(By.XPATH, badrequest_txt_xpath).text

        self.wait.until(ec.element_to_be_clickable((By.XPATH, unauthorized_link_xpath))).click()
        assert 'Link has responded with staus 401 and status text Unauthorized' == self.driver.find_element(By.XPATH,authorize_txt_xpath).text

        self.wait.until(ec.element_to_be_clickable((By.XPATH, forbidden_link_xpath))).click()
        assert 'Link has responded with staus 403 and status text Forbidden' == self.driver.find_element(By.XPATH,bidden_txt_xpath).text

        self.wait.until(ec.element_to_be_clickable((By.XPATH, notfound_link_xpath))).click()
        assert 'Link has responded with staus 404 and status text Not Found' == self.driver.find_element(By.XPATH,notfound_txt_xpath).text

        self.loggers.info("******TC006.2-Elements -Links -Existing Tab - Passed*******")