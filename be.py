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


def khoitao():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    #chrome_options.headless = True
    return webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)


def login(driver):
    driver.set_window_position(random.randint(0,1200),random.randint(0,500))
    driver.get('https://web.telegram.org/z/')
    time.sleep(20)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/button').click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[4]').click()
    except:
        return login(driver)



def change_avatar(file_name):
    driver = khoitao()
    try:
        login(driver)
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/label/input').send_keys(file_name)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/button').click()
    except:
        driver.close()
        return change_avatar(file_name)
        



def change_name(file_name):
    data = file_name.split(';')
    driver = khoitao()
    try:
        login(driver)
        time.sleep(5)
        if file_name[0] == ';':
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/button').click()
            time.sleep(2)
            for i in range(50):
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/input').send_keys(Keys.BACK_SPACE)
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/input').send_keys(data[1])
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/button').click()
        else:
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/label/input').send_keys(data[0])
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/button').click()
            time.sleep(2)
            for i in range(50):
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/input').send_keys(Keys.BACK_SPACE)
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/input').send_keys(data[1])
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[2]/div[2]/button').click()
    except:
        driver.close()
        return change_name(file_name)

def join__(link_gr):
    list_gr = link_gr.split(';')
    driver = khoitao()
    try:
        login(driver)
        for link in list_gr:
            driver.get(link)
            time.sleep(5)
            url = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[6]/a').get_attribute('href')
            driver.get(url)
            time.sleep(5)
            if driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/button[1]').text == 'JOIN GROUP':
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/button[1]').click()
                time.sleep(5)
    except:
        driver.close()
        return join__(link_gr)

def chat(data):
    loaddt = data.split('@h#1')
    driver = khoitao()
    try:
        login(driver)
        try:
            list_gr = loaddt[0].split(';')
        except:
            list_gr = loaddt[0]
        try:
            list_chat = loaddt[1].split('|')
        except:
            list_chat = loaddt[1]
        try:
            time_nghi = int(loaddt[2])
        except:
            time_nghi = 5


        for link in list_gr:
            driver.get(link)
            time.sleep(5)
            url = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[6]/a').get_attribute('href')
            driver.get(url)
            time.sleep(5)
            if driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/button[1]').text == 'JOIN GROUP':
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/button[1]').click()
                time.sleep(5)
            try:
                for chat_cm in list_chat:
                    driver.find_element_by_id('editable-message-text').send_keys(chat_cm)
                    time.sleep(1)
                    driver.find_element_by_id('editable-message-text').send_keys(Keys.ENTER)
                    time.sleep(time_nghi)
            except:
                pass
    except:
        driver.close()
        return chat(data)