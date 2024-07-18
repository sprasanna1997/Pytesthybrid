import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Utility.Logging import LogGen
from Utility.Readdata import Readdata


#XPATHS

#-------------------Browser Windows-------------------------------

alerts_btn_xpath='//button[text()=" Alerts, Frames & Windows "]'
browserwindows_btn_xpath='//a[text()=" Browser Windows"]'
newtab_btn_xpath='//button[text()="New Tab"]'
newWindow_btn_xpath='//button[text()="New Window"]'
newWindowMsg_btn_xpath='//button[text()="New Window Message"]'
getTxt_txt_xpath='//h1[@class="mb-3 fw-normal border-bottom text-left pb-2 mb-4"]'

#-------------------Alerts-------------------------------
alerts1_btn_xpath='//a[text()=" Alerts"]'
alertclick_btn_xpath='//button[text()="Alert"]'
alertdelay_btn_xpath='(//button[text()="Click Me"])[1]'
alerttext_btn_xpath='(//button[text()="Click Me"])[2]'
alertinput_btn_xpath='(//button[text()="Click Me"])[3]'
alerttext_text_xpath='//div[@id="desk"]'


#-------------------Frames-------------------------------
frames_btn_xpath='//a[text()=" Frames"]'

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

    def alerts(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, alerts_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, alerts1_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, alertclick_btn_xpath))).click()
        alert_txt=self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        print(alert_txt)
        assert alert_txt=='Hello world!','Alert text is wrong'
        self.logger.info("******TC014.1-Alerts, Frames & Windows -Alert Text Capture- Passed*******")


        self.wait.until(ec.element_to_be_clickable((By.XPATH, alertdelay_btn_xpath))).click()
        time.sleep(6)
        alert_txt = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        print(alert_txt)
        assert alert_txt == 'Hello just appeared', 'Alert text is wrong'
        self.logger.info("******TC014.2-Alerts, Frames & Windows -Alerts Delay Capture- Passed*******")


        self.wait.until(ec.element_to_be_clickable((By.XPATH, alerttext_btn_xpath))).click()
        self.driver.switch_to.alert.accept()
        alert_txt=self.driver.find_element(By.XPATH,alerttext_text_xpath).text
        assert alert_txt=='You pressed OK!','Alert text is wrong'
        self.wait.until(ec.element_to_be_clickable((By.XPATH, alerttext_btn_xpath))).click()
        self.driver.switch_to.alert.dismiss()
        alert_txt = self.driver.find_element(By.XPATH, alerttext_text_xpath).text
        assert alert_txt == 'You pressed Cancel!', 'Alert text is wrong'
        self.logger.info("******TC014.3-Alerts, Frames & Windows -Alerts Accept & Delay Capture- Passed*******")

        self.wait.until(ec.element_to_be_clickable((By.XPATH, alertinput_btn_xpath))).click()
        self.driver.switch_to.alert.send_keys(Readdata.username())
        self.driver.switch_to.alert.accept()
        self.logger.info("******TC014.3-Alerts, Frames & Windows -Alerts Entering Input Values- Passed*******")

    def frames(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, alerts_btn_xpath))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH,frames_btn_xpath))).click()
        self.driver.switch_to.frame(0)
        frames_txt=self.driver.find_element(By.XPATH,"//div /h1").text
        assert frames_txt=='Selenium - Automation Practice Form','Unable to Locate the Iframe Text'
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(0)
        frames2_txt = self.driver.find_element(By.XPATH, "//div /h1").text
        assert frames2_txt == 'Selenium - Automation Practice Form', 'Unable to Locate the Iframe Text'
        self.logger.info("******TC015-Alerts, Frames & Windows -Frame- Passed*******")





