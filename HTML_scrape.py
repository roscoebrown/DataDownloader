from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

driver = webdriver.Chrome("D:\Python\chromedriver_win32\chromedriver.exe")

link1 =   'https://cogcc.state.co.us/data2.html#/downloads'
link2 =    'https://cogcc.state.co.us/documents/data/downloads/Dashboard/DAD_Export.zip'
driver.minimize_window()
driver.get(link2)
# this needs to last for a long enough time to download the file
time.sleep(20)
driver.close()



def __init__():

    driver = webdriver.Chrome("D:\Python\chromedriver_win32\chromedriver.exe")

    link1 =   'https://cogcc.state.co.us/data2.html#/downloads'
    link2 =    'https://cogcc.state.co.us/documents/data/downloads/Dashboard/DAD_Export.zip'
    driver.minimize_window()
    driver.get(link1)
    time.sleep(5)

    '''
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
    '''
    driver.quit()
    return 
