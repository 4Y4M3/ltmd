from get_chrome_driver import GetChromeDriver
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

get_driver = GetChromeDriver()
get_driver.install()

def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

driver = driver_init()

wait = WebDriverWait(driver=driver, timeout=30)

driver.get('https://www.fmyokohama.co.jp/program/listentomydark')

# 要素が全て検出できるまで待機する
wait.until(EC.presence_of_all_elements_located)

result = driver.find_element(By.XPATH, '//*[@id="container"]/main/div[3]/div[2]/span').text

print(driver.current_url)
print(result)
driver.quit()

with open('README.md', 'w') as f:
    f.write(result)
