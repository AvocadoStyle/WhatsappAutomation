import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class wabot:
    def __init__(self, PATH):
        self._PATH = PATH
        self._waPATH = "https://web.whatsapp.com/"

    def getDriver(self):
        driver = webdriver.Chrome(self._PATH)
        driver.get(self._waPATH)
        time.sleep(3)
        return driver
    def initialize(self):
        initialize = input("enter 'yes' if you signed in\n")
        if (initialize == "yes"):
            return True
        return False

    def _getCheckname(self, driver, name):
        search = driver.find_elements_by_class_name("TbtXF")
        for s in search:
            #find = s.find_element_by_class_name("_2pkLM")
            find = s.find_element_by_class_name("_3Dr46")
            print(find.text)
            if(find.text == name):
                time.sleep(5)
                return find
        print("ERROR")
        exit()

    def getOnline(self, driver, name):
        find = self._getCheckname(driver, name)
        find.click()
    def sendMessage(self, driver, name, contain):
        find = self._getCheckname(driver, name)
        find.click()
        time.sleep(5)
        message = find.find_element_by_class_name("_2_1wd copyable-text selectable-text")

        time.sleep(1)
        print("checkcheck\n")
        time.sleep(1)
        while(True):
            message.send_keys(contain)
            message.send_keys(Keys.RETURN)
            time.sleep(1)






        search = driver.find_element_by_class_name("_35k-1 _1adfa _3-8er")
        "_7yrSq _3-8er selectable-text copyable-text"
        time.sleep(2)
        text = search.text
        time.sleep(2)
        print(text)





    def close(self, driver):
        driver.quit()

