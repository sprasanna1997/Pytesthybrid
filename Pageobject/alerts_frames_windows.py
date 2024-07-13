import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Utility.Logging import LogGen


#XPATHS

#-------------------Alerts-------------------------------

alerts_btn_xpath='//button[text()=" Alerts, Frames & Windows "]'
browserwindows_btn_xpath='//a[text()=" Browser Windows"]'
newtab_btn_xpath='//button[text()="New Tab"]'
newWindow_btn_xpath='//button[text()="New Window"]'
newWindowMsg_btn_xpath='//button[text()="New Window Message"]'
getTxt_txt_xpath='//h1[@class="mb-3 fw-normal border-bottom text-left pb-2 mb-4"]'



class Alerts_Frames_Windows:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
        self.logger=LogGen.loggen()


    def windows(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH,alerts_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, browserwindows_btn_xpath))).click()


        def window_switch(windows,cur_window):
            self.windows=windows
            self.cur_window=cur_window
            for window in self.windows:
                self.driver.switch_to.window(window)
                if self.driver.title=="Selenium Practice - Web Tables":
                    msg=self.driver.find_element(By.XPATH, getTxt_txt_xpath).text
                    self.driver.close()
                    self.driver.switch_to.window(self.cur_window)
            return msg

        self.wait.until(ec.element_to_be_clickable((By.XPATH, newtab_btn_xpath))).click()
        windows = self.driver.window_handles
        cur_window = self.driver.current_window_handle
        msg=window_switch(windows,cur_window)

        assert "New Tab"==msg,"This is not a New Tab"

        self.wait.until(ec.element_to_be_clickable((By.XPATH, newWindow_btn_xpath))).click()
        windows = self.driver.window_handles
        cur_window = self.driver.current_window_handle
        msg=window_switch(windows, cur_window)
        print(msg)
        assert "New Window" == msg, "This is not a New Window"

        self.wait.until(ec.element_to_be_clickable((By.XPATH, newWindowMsg_btn_xpath))).click()
        windows = self.driver.window_handles
        cur_window = self.driver.current_window_handle
        msg=window_switch(windows, cur_window)
        assert "New Window Message" == msg, "This is not a New Window Message"
        self.logger.info("******TC013-Alerts, Frames & Windows -Browser Windows- Passed*******")







