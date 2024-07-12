import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pageobject.forms import Forms

class TestForms:

    def test_practiceform(self,setup):
        self.driver=setup
        form_obj=Forms(self.driver)
        form_obj.practice_form()
        self.driver.quit()

    @pytest.mark.unittesting
    def test_login_and_register(self,setup):
        self.driver=setup
        login_reg_obj=Forms(self.driver)
        login_reg_obj.login_and_register()
        self.driver.quit()
