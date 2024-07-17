from Pageobject.alerts_frames_windows import Alerts_Frames_Windows
import pytest

class Test_Alerts_Frames_Windows:

    def test_browser_window(self,setup):
        self.driver=setup
        windows_obj=Alerts_Frames_Windows(self.driver)
        windows_obj.windows()
        self.driver.quit()


    def test_alerts(self,setup):
        self.driver=setup
        alerts_obj=Alerts_Frames_Windows(self.driver)
        alerts_obj.alerts()
        self.driver.quit()


