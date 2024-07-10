import pytest
from selenium import webdriver
from Pageobject.elements import Elements
from Utility.Readdata import Readdata


class Test_Elements:

    def test_textbox(self, setup):
        self.driver = setup
        txt_obj = Elements(self.driver)
        txt_obj.click_element()
        txt_obj.textbox()
    def test_checkbox(self,setup):
        self.driver=setup
        chkbox_obj=Elements(self.driver)
        chkbox_obj.checkbox_mainlevel1()
        chkbox_obj.checkbox_mainlevel2()

    def test_radiobutton(self,setup):
        self.driver=setup
        radio_obj=Elements(self.driver)
        radio_obj.radiobutton_yes()
        radio_obj.radiobutton_impressive()
        radio_obj.radiobutton_enable_check()

    def test_webtables(self,setup):
        self.driver=setup
        webtables_obj=Elements(self.driver)
        webtables_obj.webtables_add_user()
        webtables_obj.webtables_delete_user()
        webtables_obj.webtables_edit_user()
        webtables_obj.webtables_search_user()
