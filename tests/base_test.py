from unittest import TestCase
from alttester import AltDriver
from appium import webdriver
# from appium.options.android import UiAutomator2Options
import os
import time


class TestBase(TestCase):
    platform = None

    @classmethod
    def setUpClass(cls):
        if os.getenv("APPIUM_PLATFORM", "android") == 'android':
            cls.platform = 'android'
        else:
            cls.platform = 'ios'
        print("Running on " + cls.platform)
        cls.desired_caps = {}
        cls.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', cls.desired_caps)
        print("Appium driver started")
        time.sleep(10)
        cls.altdriver = AltDriver(host="insert_ip_here", port=13000) # instantiate AltDriver with the Elastic IP for the AWS EC2 Instance
        # cls.altdriver = AltDriver() # instantiate AltDriver for local connection
        
    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
        cls.driver.quit()
