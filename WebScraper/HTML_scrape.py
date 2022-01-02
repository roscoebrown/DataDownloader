from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


driver = webdriver.Chrome("D:\Python\chromedriver_win32\chromedriver.exe")

driver.minimize_window()
driver.get('https://cogcc.state.co.us/data2.html#/downloads')
time.sleep(5)

colorado_site = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(colorado_site, 'lxml')
body = soup.find_all('div', class_ = 'contentBody containerOuter')
links = soup.find('ul', class_ = "ng-scope")
print(links)

for link in links:
    file = link.find('li')
    if link == -1:
        continue
    else:
        downloads = file['href']
    # make a loop that goes over the -1 objects 
    print(downloads)
    print(' ---------------- ')

driver.quit()