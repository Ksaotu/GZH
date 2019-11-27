from appium import webdriver
import time
import pytest

class TestLogin:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "123"
        caps["appPackage"] = "com.strong.letalk"
        caps["appActivity"] = "com.strong.letalk.ui.activity.login.UserGuideActivity"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(25)
    @pytest.mark.parametrize("loginname,password,toast",[

        ('abc','a12134567','该用户不存在'),
        ('955112','a122222','密码不正确')
    ])
    def test_login(self,loginname,password,toast):
        self.driver.find_element_by_id("com.strong.letalk:id/name").send_keys(loginname)
        self.driver.find_element_by_id("com.strong.letalk:id/password").send_keys(password)
        self.driver.find_element_by_id("com.strong.letalk:id/sign_in_button").click()
        #print("断言")
        assert  self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text == toast

    def teardown(self):
        self.driver.quit()
