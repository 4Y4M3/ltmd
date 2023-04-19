from get_chrome_driver import GetChromeDriver
from selenium import webdriver

get_driver = GetChromeDriver()
get_driver.install()

def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

driver = driver_init()
driver.get('https://www.fmyokohama.co.jp/program/listentomydark')
print(driver.find_element_by_xpath('//*[@id="js__onAir"]/div/div[1]/div[1]/p').text)
print(driver.current_url)
driver.quit()
