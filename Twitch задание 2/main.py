from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

myfile = open('log.txt' , 'w')

browser = webdriver.Chrome()




search_text = "Pool"
browser.get("https://www.twitch.tv/")
searchbox = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div/div[2]/div/div/div/div/div[1]/div/div/div/input')
searchbox.send_keys(search_text)
time.sleep(5)
elems = browser.find_elements_by_xpath('//*[starts-with(@id, "search-result-row_")]/div/div/a[@href]')
for elem in elems:
    print(elem.get_attribute("href"))


searchbox.send_keys(Keys.CONTROL + "a")
searchbox.send_keys(Keys.DELETE)
searchbox.send_keys(search_text+'\n')
#//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/a
print('---------------')
time.sleep(5)
videos1 = browser.find_elements_by_xpath('//*[starts-with(@data-a-target, "search-result-live-channel")]/a[@href]')
for video in videos1:
    print(video.get_attribute("href"))
    myfile.write(video.get_attribute("href")+'\n')

print('---------------')
videos4 = browser.find_elements_by_xpath('//*[starts-with(@data-test-selector, "search-result-offline-channel__name")]/a[@href]')
for video in videos4:
    print(video.get_attribute("href"))
    myfile.write(video.get_attribute("href")+'\n')

print('---------------')
videos2 = browser.find_elements_by_xpath('//*[starts-with(@class, "ScTextMargin")]/div/a[@href]')
for video in videos2:
    print(video.get_attribute("href"))
    myfile.write(video.get_attribute("href")+'\n')
print('---------------')
videos3 = browser.find_elements_by_xpath('//*[starts-with(@data-a-target, "search-result-video")]/a[@href]')
for video in videos3:
    print(video.get_attribute("href"))
    myfile.write(video.get_attribute("href")+'\n')
print('---------------')
myfile.close()