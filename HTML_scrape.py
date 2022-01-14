from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import schedule
import threading
from datetime import date
import glob
import os
import csv
import zipfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.chrome.webdriver import WebDriver

# from webdriver_manager.chrome import ChromeDriverManager
class file_organization():

    def unzip(file_path, extract_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)  
        return

    def rename_csv(extract_path,rename_path):
        currentdate_time = str(date.today())
        os.rename(extract_path,rename_path)
        return

class bots():
        
    def run_continuously(interval=1):
        cease_continuous_run= threading.Event()
        class ScheduleThread(threading.Thread):
            @classmethod
            def run(cls):
               while not cease_continuous_run.is_set():
                    schedule.run_pending()
                    time.sleep(interval)
        
        continuous_thread = ScheduleThread()
        continuous_thread.start()
        return cease_continuous_run
    
    # this is just a test bot does not do anything
    def background_job():
        print('the bot is waiting in the background')
    
    
    def Colorado_bot(): # Colorado
        
        print("working")
        # setting the chrome options
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : "D:\Python\WebScraper\Colorado"} 
        options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome("D:\Python\chromedriver_win32\chromedriver.exe",chrome_options=options)
        link =    'https://cogcc.state.co.us/documents/data/downloads/Dashboard/DAD_Export.zip'
        driver.minimize_window
        driver.get(link)
        time.sleep(40)
        # close() closes 1 brower
        # quit() closes all selium windows ,
        currentdate_time = str(date.today())
        folderpath = "D:\Python\WebScraper\Colorado"
        file_type = '\*zip'
        files = glob.glob(folderpath+file_type)
        max_file = max(files,key = os.path.getctime)
        os.rename(max_file,'D:\Python\WebScraper\Colorado\Colorado_'+currentdate_time+'_.zip')
        file_organization.unzip('D:\Python\WebScraper\Colorado\Colorado_'+currentdate_time+'_.zip','D:\Python\WebScraper\Colorado\Extract\Colorado_'+currentdate_time)
        file_organization.rename_csv("D:\Python\WebScraper\Colorado\Extract\Colorado_2022-01-12\dailyActivityDashboard.xlsx",'D:\Python\WebScraper\Colorado\Colorado_'+currentdate_time+'_.xlsx')
        print("working...")
        driver.close()
        return print("done")


    def California_bot(): # California
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : "D:\Python\WebScraper\California"} 
        options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome("D:\Python\chromedriver_win32\chromedriver.exe",chrome_options=options)
        link =    'https://gis.conservation.ca.gov/portal/home/item.html?id=0d30c4d9ac8f4f84a53a145e7d68eb6b'
        driver.minimize_window
        driver.get(link)
        time.sleep(30)
        download = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/main/aside/div/button[6]"))
        )
        download.click()
        currentdate_time = str(date.today())
        folderpath = "D:\Python\WebScraper\California"
        file_type = '\*zip'
        files = glob.glob(folderpath+file_type)
        max_file = max(files,key = os.path.getctime)
        # make this an f string
        os.rename(max_file,'D:\Python\WebScraper\California\California_'+currentdate_time+'_.zip')
        driver.close()
        return print('done')


# make a code to extract the files and put them into a pandas dataframe


# start the background thread it will continue to run forever
#stop_run_continously = run_continuously()

# this will make it stop running
#stop_run_continously.set()


'''
Extra Code
this is for selecting anything with cookies
        gotit = driver.find_element_by_id('accept-cookie-notifcation')
        gotit.click()
        downloadcsv = driver.find_element_by_css_selector('.icon-csv')
        downloadcsv.click
         this needs to last for a long enough time to download the file
'''