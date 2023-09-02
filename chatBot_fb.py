from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from config import username, password, send_user1
from sms_users_fb import sms


service = Service(exsecutive_path='/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)


try:
    driver.get('https://www.facebook.com/messages/t/')
    time.sleep(5)

    userI = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[1]/'
                                                   'input')
    userI.clear()
    userI.send_keys(username)
    time.sleep(5)
    userP = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/div/div[3]/div[2]/form/div[2]/div[2]/'
                                                   'div/div/input')
    userP.clear()
    userP.send_keys(password)
    time.sleep(5)
    userP.send_keys(Keys.ENTER)
    time.sleep(20)

    enter_user = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/'
                                                        'div[1]/div/div/div/div/div[2]/div/div/div/div/div/label/input')
    time.sleep(5)
    enter_user.send_keys(send_user1)
    time.sleep(10)
    user = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/'
                                                  'div[1]/div[1]/div/div[1]/ul/li[1]/ul/div[2]/li/div/a/div/div[2]/div/'
                                                  'div/div/span/span/span')
    user.click()
    time.sleep(20)

    text = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/'
                                                  'div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/'
                                                  'div[4]/div[2]/div/div/div[1]/p')
    text.send_keys(sms)
    time.sleep(5)
    text.send_keys(Keys.ENTER)
    time.sleep(15)

    driver.close()
    driver.quit()

except Exception as ex:
    print(ex)




