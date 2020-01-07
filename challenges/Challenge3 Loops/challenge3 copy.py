import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

    def tearDown(self):
        self.driver.close()
        print "in tear down"

    def test_challenge3whileloop(self):
        # self.driver.get("https://www.copart.com")
        # wait = WebDriverWait(self.driver, 15)
        # wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Trending")))
        elements = self.driver.find_elements(By.XPATH("//*[ng-if=\"popularsearches\"]/div[3]//a")


        for element in elements:
            print(element.text + " - " + element.get_property("href"))

    if __name__ == '__main__':
        unittest.main()

