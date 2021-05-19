from initialize import wabot

if __name__ == '__main__':
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    name = "ינון Java"
    contain = "test"
    times = 200
    initwa = wabot(PATH)
    driver = initwa.getDriver()
    # wait untill login
    if(initwa.initialize()):
        #initwa.getOnline(driver, name)
        initwa.sendMessage(driver, name, contain, times)
    else:
        initwa.close(driver)