from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys


file = open('log.txt', 'w', encoding="utf-8")

browser = webdriver.Chrome()

def priint():
    twitext = browser.find_elements_by_xpath('//*[starts-with(@lang, "en")]/span[1]')
    for twit in twitext:
        # print(twit.text)
        file.write(twit.text + '\n')




browser.get("https://twitter.com/elonmusk/")
time.sleep(5)

#browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
for i in range(50):
    browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    priint()



