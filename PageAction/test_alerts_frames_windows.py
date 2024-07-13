from Pageobject.alerts_frames_windows import Alerts_Frames_Windows

class Test_Alerts_Frames_Windows:

    def test_alerts(self,setup):
        self.driver=setup
        windows_obj=Alerts_Frames_Windows(self.driver)
        windows_obj.windows()
        self.driver.quit()
