from selenium import webdriver

def goTo(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome("assets/chromedriver",chrome_options = chrome_options)
    driver.get(url)


# goTo("https://www.google.com/maps/dir/40.4432978,-79.9455097/Shirley+Apartments,+North+Dithridge+Street,+Pittsburgh,+PA/@40.4455577,-79.9506551,17z/data=!4m25!4m24!1m16!3m4!1m2!1d-79.9472673!2d40.445939!3s0x8834f2240aa136f5:0xa3edf909f613763a!3m4!1m2!1d-79.9511066!2d40.4447158!3s0x8834f22671c3d413:0xf38fa85842361561!3m4!1m2!1d-79.9498959!2d40.446292!3s0x8834f2243458261b:0x1a2f2a3471106670!4e1!1m5!1m1!1s0x8834f2250ab9e27f:0xd8e954f5bdc80565!2m2!1d-79.9514292!2d40.4477082!3e2")