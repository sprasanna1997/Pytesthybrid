import pytest
from selenium import webdriver
from Pageobject.elements import Elements
from Utility.Readdata import Readdata


class Test_Elements:


    def test_textbox(self, setup):
        self.driver = setup
        ele_obj = Elements(self.driver)
        ele_obj.click_element()
        ele_obj.filling_checkbox()

