#!/usr/bin/env python
# coding: utf-8

# In[14]:


# from grabRigData import grabtxrrcdata
from postgresCheck import postgresCheck
# from postgresPush import pushRigs


import re
import os
import ast
import PyPDF2 as p2
from pdfminer.high_level import extract_text
import pandas as pd
from pdfminer.converter import TextConverter
import ocrmypdf

import timeit
import time


# In[15]:


class fahimsCrawler():
    
    def __init__(self,path ='C:/Users/Fahim/Desktop/Gibson Reports/AI/Temp3'):
        self.path = path
        os.chdir('C:/Users/Fahim/Desktop/Gibson Reports/AI')
        
        file = open("companyDict.txt","r")
        contents = file.read()
        self.companyDict = ast.literal_eval(contents)
        file.close()
        
        os.chdir(self.path)
        self.rigdb = pd.DataFrame(columns = ['externalattachmentid','rigname'])
#         path, dirs, files = next(os.walk(self.path))
#         self.count = len(files) #count number of files in the directory
    
    
    ###########                             ocr  (optional level)                                ####################   
    
    def ocr(self,filename):
        
        ocrmypdf.ocr(filename,filename,force = True)
        
        return
    
    ###########                     crosscheck sql and extract rig name                         ####################
    
    def getMethod(self,company):
        
        methodName = self.companyDict[company] #returns a list
        module = 'rigExtractor'
        
#         print(methodName)
        
#         importedMethodList = []
        instanceMethodList = []
        
        for imports in methodName:
    
            method = getattr(__import__(module, fromlist=[imports]), imports) 
            m = method()
            instanceMethodList.append(m)
            
            
        
        return instanceMethodList
        
    
    def crawl(self):
        pg = postgresCheck() # instantiating postgresCheck class
        
        count = 0
        
        for file in os.listdir(self.path):
            if file.endswith('.pdf'):
                
                count += 1
                ID = file.split('_')[2].replace('.pdf','')
                
                print('Processing File Numner: ',count,'----------------------------------------------\n')
                
                tags = pg.checkFile(file) #using postgresCheck class
    
                if tags != 'missing':
                    if tags[1] != 'OTHER':
                    
                        if pg.checkRig(file) == 'missing':
                    
                            try:
                                os.chdir(self.path)

                                methodsList = self.getMethod(tags[0])

                                rigName= None

                                for method in methodsList:
                                    if rigName == None:
                                        rigName = method.main(file)


    #                             print(tags[0],file,rigName)

                                if rigName != None:
                                    self.rigdb = self.rigdb.append({'externalattachmentid':ID, 'rigname':rigName} , ignore_index = True)
                                    print('Rig Added!')



                            except Exception as ex:
                                print('\n',ex,file,'\n' )
                        else:
                            print('Already crawled')
                            
#                 else:
#                     print('Document not found in postgres database!')
                            
        pg.cur1.close()
        pg.cur2.close()
        pg.conn.close()
        
        return self.rigdb
    
    ###########                      Push rig names to sql database                         ####################
    def push(self):
        
        pr = pushRigs()
        pr.push(self.rigdb)
        
        return
    
    ###########                      Main program to execute the class                        ####################
    
    def main(self):
        return
    
        
        
                                         
                            
                        


# In[ ]:





# In[ ]:


## Running program without using main:


# In[16]:


os.chdir('C:/Users/Fahim/Desktop/Gibson Reports/AI/Temp3')


# In[17]:


tik = time.perf_counter()
f = fahimsCrawler()
rigs = f.crawl()
tok = time.perf_counter()
print('The program took', tok-tik, 'seconds to run')


# In[ ]:





# In[ ]:





# In[19]:


rigs = f.rigdb


# In[20]:


rigs['rigname'] = rigs['rigname'].str.upper()
rigs['rigname'] = rigs['rigname'].str.strip()


# In[23]:


# print(rigs)


# In[ ]:





# In[24]:


os.chdir('C:/Users/Fahim/Desktop/Gibson Reports/AI') ## export path
rigs.to_csv('Rigsv8.csv',index = False)


# In[ ]:




