from selenium import webdriver
# from selenium.webdriver.common.keys import keys
import time 
browser = webdriver.Chrome("C:\\Users\\uncor\\Desktop\\automation-project\\chromedriver.exe")
browser.get('http://www.google.com/xhtml')
time.sleep(5)  # Let the user actually see something!
search_box = browser.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
browser.quit()
