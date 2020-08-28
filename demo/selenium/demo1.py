# coding=utf-8
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("G:/pywork/chromedriver.exe")


def test1():
    browser = webdriver.Chrome("G:/pywork/chromedriver.exe")
    browser.get("https://blog.csdn.net")
    print(browser.page_source)
    browser.close()


def query():
    browser = webdriver.Chrome("G:/pywork/chromedriver.exe")
    browser.get("http://www.baidu.com")
    input_str = browser.find_element_by_id('kw')
    input_str.send_keys("MakBook pro")
    time.sleep(2)

    button = browser.find_element_by_id('su')
    ss = button.click()
    time.sleep(1)
    title = browser.title
    print(title)
    user = browser.find_element_by_class_name('t').text
    print(user)


def test2():
    driver = webdriver.Chrome("G:/pywork/chromedriver.exe")
    first_url = "http://www.baidu.com"
    driver.get(first_url)
    print("now access   %s" % first_url)
    # 访问新闻网页，
    second_url = "http://news.baidu.com"
    print("now access %s" % (second_url))
    driver.get(second_url)
    # 返回到百度首页
    print("back to %s" % (first_url))
    driver.back()
    # 前进到新闻页
    print('forward to  %s ' % second_url)
    driver.forward()
    driver.quit()


def test3():
    driver = webdriver.Chrome("G:/pywork/chromedriver.exe")
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").clear();
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    driver.quit()


def test4():
    driver = webdriver.Chrome("G:/pywork/chromedriver.exe")
    driver.get("https://www.baidu.cn")
    # 定位到要悬浮的元素位置
    above = driver.find_element_by_link_text("设置")
    # 对定位 到元素执行鼠标悬浮澳洲
    ActionChains(driver).move_to_element(above).perform()
    ActionChains(driver).context_click()
    time.sleep(30)


def test5():
    driver.get("http:/www.baidu.com")
    # 输入框内容
    driver.find_element_by_id("kw").send_keys("seleniumm")
    # 删除多输入的一个m
    time.sleep(3)
    driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)


def test6():
    driver.get("https://www.baidu.com")
    print(" before  search --------")
    title = driver.title

    # 打印当前页面的url
    now_url = driver.current_url
    print(now_url)
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    time.sleep(1)
    print('After search================')

    # 再次打印当前页面的title
    title = driver.title
    print(title)

    # 打印当前页面URL
    now_url = driver.current_url
    print(now_url)

    # 获取结果数目
    user = driver.find_element_by_class_name('nums').text
    print(user)

    driver.quit()


def test7():
    driver.get("https://www.baidu.com")
    element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))
    element.send_keys("seleminu")


def test8():
    driver.get("http://www.baidu.com")
    try:
        print(time.ctime())
        driver.find_element_by_id("kw2xx2").send_keys('selenium')
    except NoSuchElementException as e:
        print(e)
    finally:
        print(time.ctime())
        driver.quit()


def testxpath():
    driver.get("https://www.baidu.com")

    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    time.sleep(1)

    # 定位一组元素
    texts = driver.find_elements_by_xpath('//div/h3/a')

    # 循环遍历出每一条搜索结果的标题
    for t in texts:
        print(t.text)


def test163():
    driver.get("https://email.163.com")
    # time.sleep(5)
    # driver.switch_to.frame('x-URS-iframe1556522384056.9438')



    time.sleep(6)
    driver.quit()


if __name__ == '__main__':
    test163()
