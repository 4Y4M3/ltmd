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

driver.get('https://twitter.com/ltmd847')

# 要素が全て検出できるまで待機する
wait.until(EC.presence_of_all_elements_located)

result = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div').text

print(driver.current_url)
print(result)
driver.quit()

with open('README.md', 'w') as f:
    f.write(result)
