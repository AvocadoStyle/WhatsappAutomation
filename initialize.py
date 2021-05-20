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
        time.sleep(3)

        #check = driver.find_elements_by_class_name("YmixP fKfSX")
        check = driver.find_elements_by_class_name("_7yrSq _3-8er selectable-text copyable-text")
        print(check.text)

        #"_2uaUb" # for the main for the status and all the items
        #"_1-qgF"

        #"YmixP fKfSX" # for the status



    def sendMessage(self, driver, name, contain, times):
        counter = 0
        find = self._getCheckname(driver, name)
        find.click()
        time.sleep(1)
        # message = driver.find_element_by_class_name("_2A8P4")
        while(counter != times):
            message = driver.find_element_by_class_name("_2A8P4")
            con = contain
            contain = contain + str(counter)
            message.send_keys(contain)
            message.send_keys(Keys.RETURN)
            time.sleep(1)
            counter += 1
            contain = con

    def close(self, driver):
        driver.quit()

