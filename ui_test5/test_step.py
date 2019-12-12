import yaml
from appium import webdriver
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

class TestLogin:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "123"
        caps["appPackage"] = "com.strong.letalk"
        caps["appActivity"] = "com.strong.letalk.ui.activity.login.UserGuideActivity"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(25)

    def test_loginstep(self):
        TestStep("login_step.yaml").run(self.driver)

    def teardown(self):
        self.driver.quit()

class TestStep:
    def __init__(self, path):
        file = open(path, encoding='utf-8')
        self.steps=yaml.safe_load(file)

    def run(self,driver: WebDriver):
        for step in self.steps:
            if isinstance(step,dict):
                element=None
                if "id" in step.keys():
                    element = driver.find_element_by_id(step['id'])
                elif "xpath" in step.keys():
                    element = driver.find_element_by_xpath(step['xpath'])
                else:
                    print(step.keys())
                if 'input' in step.keys():
                    element.send_keys(step['input'])
                elif 'get' in step.keys():
                    text = element.get_attribute(step['get'])
                    print(text)
                if 'assert' in step.keys():
                    print(step['assert'])
                    assert element.get_attribute(step['get']) == step['assert']
                else:
                    element.click()





