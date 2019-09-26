import unittest
from modle.driver import Chrome
import time


class MyTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     d = Chrome()
    #     cls.driver = d.browser_chrome()

    # @classmethod
    # def tearDownClass(cls):
    #     pass

    def setUp(self):
        d=Chrome()
        self.driver=d.browser_chrome()

    def tearDown(self):
        self.driver.quit()