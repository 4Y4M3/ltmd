from get_chrome_driver import GetChromeDriver
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

get_driver = GetChromeDriver()
get_driver.install()

url = 'https://nitter.net/ltmd847'

def driver_init():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)

driver = driver_init()
driver.implicitly_wait(10)

driver.get(url)

WebDriverWait(driver, 15).until(EC.visibility_of_element_located(By.CLASS_NAME, 'timeline-item'))
elems_item = driver.find_elements(By.CLASS_NAME, 'timeline-item')

print(len(elems_item))

tweet_list = []
for elem_item in elems_item:
    link = elem_item.find_element(By.CLASS_NAME, 'tweet-link').get_attribute("href")
    tweet = elem_item.find_element(By.CLASS_NAME, 'tweet-body').text
            
    info = {}
    info["link"] = link
    info["tweet"] = tweet
    
    tweet_list.append(info)

tweets = "\n".join(map(str,tweet_list))

print(driver.current_url)
print(tweets)
driver.quit()

with open('README.md', 'w') as f:
    f.write(tweets)
