from initialize import wabot

if __name__ == '__main__':
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    name = "ינון Java"
    contain = "test\n\n"
    initwa = wabot(PATH)
    driver = initwa.getDriver()
    # wait untill login
    if(initwa.initialize()):
        #initwa.getOnline(driver, name)
        initwa.sendMessage(driver, name, contain)
    else:
        initwa.close(driver)