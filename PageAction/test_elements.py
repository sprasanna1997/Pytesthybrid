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
        self.driver.quit()
    def test_checkbox(self,setup):
        self.driver=setup
        chkbox_obj=Elements(self.driver)
        chkbox_obj.checkbox_mainlevel1()
        chkbox_obj.checkbox_mainlevel2()
        self.driver.quit()

    def test_radiobutton(self,setup):
        self.driver=setup
        radio_obj=Elements(self.driver)
        radio_obj.radiobutton_yes()
        radio_obj.radiobutton_impressive()
        radio_obj.radiobutton_enable_check()
        self.driver.quit()

    def test_webtables(self,setup):
        self.driver=setup
        webtables_obj=Elements(self.driver)
        webtables_obj.webtables_add_user()
        webtables_obj.webtables_delete_user()
        webtables_obj.webtables_edit_user()
        webtables_obj.webtables_search_user()
        self.driver.quit()

    def test_buttons(self,setup):
        self.driver=setup
        buttons_obj=Elements(self.driver)
        buttons_obj.buttons_single_click()
        buttons_obj.buttons_right_click()
        buttons_obj.buttons_double_click()
        self.driver.quit()

    def test_links(self,setup):
        self.driver=setup
        links_obj=Elements(self.driver)
        links_obj.links_new_tab()
        links_obj.links_existing_tab()
        self.driver.quit()

    def test_brokenlinks(self,setup):
        self.driver=setup
        brokenlink_obj=Elements(self.driver)
        brokenlink_obj.broken_links()
        self.driver.quit()

    def test_upload_and_download(self,setup):
        self.driver=setup
        upload_obj=Elements(self.driver)
        upload_obj.upload_and_download()
        self.driver.quit()

    def test_dynamic_properties(self,setup):
        self.driver=setup
        dynmprop_obj=Elements(self.driver)
        dynmprop_obj.dynomic_properties()
        self.driver.quit()

