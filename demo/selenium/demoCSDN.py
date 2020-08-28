import time

from retrying import retry
from selenium import webdriver

@retry(stop_max_attempt_number=3)
def getToCsdn():
    time.sleep(30)
    options = webdriver.ChromeOptions()
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
        }
    }
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path="G:/pywork/chromedriver.exe", options=options)
    count = 0
    while True:
        driver.get("https://blog.csdn.net/yumingzhu1/article/details/108254255")
        time.sleep(20)
        js = 'window.scrollTo(0,500)'
        driver.execute_script(js)
        time.sleep(10)
        time.sleep(30)
        count = count + 1
        print(count)
        driver.back()

if __name__ == '__main__':
    getToCsdn()
