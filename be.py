from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType


def khoitao():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    return webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)


def login(driver):
    driver.get('https://web.telegram.org/z/')
    time.sleep(10)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[4]').click()
    except:
        return login(driver)




def change_avatar(file_name):
    driver = khoitao()
    login(driver)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/label/input').send_keys(file_name)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/button').click()
    


