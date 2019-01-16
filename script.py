from selenium import webdriver
# from selenium.webdriver.common.keys import keys
import time 

browser = webdriver.Chrome("C:\\Users\\uncor\\Desktop\\automation-project\\chromedriver.exe")

def login(self,username,password,captchaloc):
    browser.get('https://www.swagbucks.com/')
    time.sleep(5)  # Let the user actually see something!
    username = browser.find_element_by_id('sbxJxRegEmail').send_keys('pythontest667@gmail.com')
    password = browser.find_element_by_id('sbxJxRegPswd').send_keys('roxxy123')
    captchaloc = browser.find_element_by_class_name('recaptcha-checkbox-checkmark').click
    time.sleep(20)  # Let the user actually see something!
    browser.quit()

