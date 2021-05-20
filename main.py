from initialize import wabot

if __name__ == '__main__':
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    name1 = "ינון Java"
    name2 = "לומדים ביחד-מדעי המחשב"
    contain = "test"
    times = 200
    initwa = wabot(PATH)
    driver = initwa.getDriver()
    # wait untill login
    if(initwa.initialize()):
        # initwa.getOnline(driver, name2)
        initwa.sendMessage(driver, name2, contain, times)
    else:
        initwa.close(driver)