#!/usr/bin/env python
# coding: utf-8

# This script will connect to the texas rrc FTP server and download all the files onto a local drive.

# In[1]:


import requests
from ftplib import FTP
from datetime import datetime
from datetime import timedelta
import zipfile
import os
import ast


# In[6]:


#a python class to scape data from the texas rrc file transfer protocol

class grabtxrrcdata():
    
    def __init__(self, storagePath = 'C:/Users/Fahim/Desktop/Gibson Reports/AI/Temp3',
                        configPath = 'C:/Users/Fahim/Desktop/Gibson Reports/AI'):
        
        self.url = 'ftpe.rrc.texas.gov'
        self.username = 'anonymous'
        self.password = 'email@email.com'
        
        os.chdir(configPath) 
        
        dateFile = open("LastUpdate.txt","r")
        contents = dateFile.read()
        dateDict = ast.literal_eval(contents)
        self.date = datetime(dateDict['Year'],dateDict['Month'],dateDict['Day'])  #just change this to the day after the last updated day
        dateFile.close()
        
        today = datetime.today()
        deltaT = today - self.date
        self.days = deltaT.days     
        
        newDict = {'Year':datetime.today().year,'Month':datetime.today().month,'Day':datetime.today().day}
        with open('LastUpdate.txt', 'w') as f:
            print(newDict, file=f)
    
        os.chdir(storagePath) 
        
    def login(self):
        global ftp 
        
        ftp = FTP(self.url)
        ftp.login(self.username, self.password)
        return
    
    def makeLabel(self):
        self.dirName = self.date.strftime('%x').replace('/','-') + '20'
        self.fileName = self.dirName + '.zip'
        print(self.dirName)
        
        return
    
    def changeDate(self):
        self.date = self.date  + timedelta(days=1)
        return
    
    def setDir(self):
        ftp.cwd(str('/directional_survey/' + self.dirName + '/'))
        return
    
    def grabFile(self):
        localFile = open(self.fileName, 'wb')
        ftp.retrbinary('RETR ' + self.fileName, localFile.write, 1024)
        ftp.quit()
        localFile.close()
        return
    
    def unzipFile(self):
        zfile = zipfile.ZipFile(self.fileName)
        zfile.extractall()
        zfile.close()
        os.remove(self.fileName)
        return
    
    def main(self):
        
        for day in range(self.days):
            self.login()
            self.makeLabel()
            self.setDir()
            self.grabFile()
            self.unzipFile()
            self.changeDate()
            print(self.dirName + ' done!')

            
        return        


# In[7]:


t = grabtxrrcdata()


# In[8]:


t.main()


# In[5]:




