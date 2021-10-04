from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
import random
import threading


def khoitao():
                chrome_options = webdriver.ChromeOptions()
                prefs = {"profile.default_content_setting_values.notifications" : 2}
                chrome_options.add_experimental_option("prefs",prefs)
                #chrome_options.headless = True
                return webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)

def login(driver):
                driver.set_window_position(0,0)
                driver.get('https://web.telegram.org/z/')
                time.sleep(20)
                try:
                        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/button').click()
                        time.sleep(5)
                        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[4]').click()
                        time.sleep(5)
                        ten_acc = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/h3').text
            
                except:
                        return login(driver)

driver = khoitao()
login(driver)
driver.get('https://web.telegram.org/z/#-527898122')
time.sleep(1)
driver.refresh()
time.sleep(5)
element1 = driver.find_elements_by_class_name('Message message-list-item first-in-group last-in-group open shown').text
print(element1)
for el in element1:
        print(el)