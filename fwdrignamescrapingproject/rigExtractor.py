#!/usr/bin/env python
# coding: utf-8

# # <Center>Regex Library<Center>

# In[1]:


import re
from pdfminer.high_level import extract_text
import ocrmypdf

import os
os.chdir('C:/Users/Fahim/Desktop/Gibson Reports/AI/Temp2')


# ## Method 1 (Compass)
# 
# 1) PHOENIX TECHNOLOGY SERV USA INC. | 
# 2) SCIENTIFIC DRILLING INT'L, INC. | 
# 3) QES DIRECTIONAL DRILLING, LLC |
# 3) ALTITUDE ENERGY PARTNERS, LLC |
# 4) CATHEDRAL ENERGY SERVICES INC. |
# 5) AIM DIRECTIONAL SERVICES, LLC | 
# 6) CHOICE DIRECTIONAL SVCS US CORP. |
# 7) NABORS DRILLING TECH USA, INC. | 
# 7) METEORITE ENERGY SERVICES INC.
# 8) INTREPID D.D.S., LTD. |
# 9) PROFESSIONAL DIRECTIONAL ENT INC | 
# 10) DEFINITIVE DIRECTIONAL , LLC

# In[5]:


class method1():
    
    def __init__(self):
        self.regex =  re.compile(r'@\s+\w+\.\w+\s+\(\w+.*')
        return
    
    def main(self,filename):
        text = extract_text(filename,page_numbers = [2])
        
        rig_name = None
        
        for line in text.split('\n'):
            
            match = self.regex.search(line)
            
            if match != None:
                
                rig_name = match.group(0).split('(',)[1].replace(')','')
                
                                
                if rig_name.find('GL') != -1:
                    rig_name = match.group(0).split('(',)[2].replace(')','')
                
                return rig_name
            
        if rig_name == None:
            
            text = extract_text(filename,page_numbers = [5])
            
            for line in text.split('\n'):
                
                match = self.regex.search(line)
                
                if match != None:
                    
                    rig_name = match.group(0).split('(',)[1].replace(')','')
                    
                    return rig_name
            
            
        


# In[1]:


# m = method1()
# name = m.main('dir_survey_5181847.pdf')
# name


# In[ ]:





# ## Method 2
# 
# 1) VAUGHN ENERGY SERVICES |
# 2) ACCURATE DIRECTIONAL |
# 3) GEO-MAG MWD LLC

# In[1]:


class method2():
    
    def __init__(self):
        self.regex =  re.compile(r'Rig\s+Name:\s+\w+.*')
        return
    
    def main(self,filename):
        text = extract_text(filename,page_numbers = [0])
        
        rig_name = None
        
        for line in text.split('\n'):
            
            match = self.regex.search(line)
            
            if match != None:
                
                rig_name =  match.group(0).split(':')[1].strip()
                
                return rig_name
            
        if rig_name == None:
            text = extract_text(filename,page_numbers = [2])
            
            for line in text.split('\n'):
            
                match = self.regex.search(line)

                if match != None:

                    rig_name =  match.group(0).split(':')[1].strip()

                    return rig_name
            
            


# In[ ]:





# ## Method 3
# 
# 1) GEO-MAG MWD LLC |
# 2) LEGACY DIRECTIONAL DRILLING, LLC

# In[31]:


class method3():
    
    def __init__(self):
        self.regex = re.compile(r'Rig\s+ID:\s+\w+.*')
        self.regex2 = re.compile(r'Rig\s+ID:')
        return
    
    def main(self,filename):
        text = extract_text(filename,page_numbers = [0])
        
        rig_name = None
        
        lines = []
        
        for line in text.split('\n'):
            lines.append(line)
        
        for line in lines:
            
            match = self.regex.search(line)
            
            if match != None:
                
                rig_name =  match.group(0).replace('Rig ID: ','').strip()
                
                return rig_name
            
            
            
        if rig_name == None:
            
            count = 0
            
            for line in lines:
                
                count +=1
            
                match = self.regex2.search(line)
                
                if match != None:
                    
                    rig_name = lines[count+1]

                    return rig_name
            
            
            


# In[77]:


# m = method3()
# name = m.main('dir_survey_5104999.pdf')
# name


# In[ ]:





# ## Method 4
# 1) GORDON TECHNOLOGIES |
# 2) KOLTEK ENERGY SERVICES, LLC

# In[2]:


class method4():
    
    def __init__(self):
        self.regex =  re.compile(r'Rig:\s+\w+.*')
        return
    
    def main(self,filename):
        
        ocrmypdf.ocr(filename,filename,force=True)
        
        text = extract_text(filename,page_numbers = [0])
        
        for line in text.split('\n'):
            
            match = self.regex.search(line)
            
            if match != None:
                
                rig_name =  match.group(0).replace('Rig: ','').strip()
                
                return rig_name
            


# In[3]:


# m = method4()
# name = m.main('dir_survey_5172547.pdf')
# name


# ## Method 5
# 1) GYRODATA

# In[9]:


class method5():
    
    def __init__(self):
        self.regex =  re.compile(r'Location:.*')
        return
    
    def main(self,filename):
        text = extract_text(filename,page_numbers = [1])
        
        for line in text.split('\n'):
            
            match = self.regex.search(line)
            
            if match != None:
                
                rig_name =  match.group(0).split(':')[1].split(',')[0]
                
                if 'well' in rig_name.lower():
                    return None
                else:
                    return rig_name
            


# In[ ]:





# ## Method 6
# 1) SCIENTIFIC DRILLING INT'L, INC.

# In[12]:


class method6():
    
    def __init__(self):
        self.regex =  re.compile(r'\d+/\d+/\d{4}') #catching a date
        return
    
    def main(self,filename):
        text = extract_text(filename,page_numbers = [0])
        
        lines = []
        
        for line in text.split('\n'):
            lines.append(line)
            
        count = 0
        
        for line in lines:
            
            count += 1
            
            match = self.regex.search(line)
            
            if match != None:
                
                rig_name =  lines[count-3]
                
                return rig_name


# ## Method 7
# 
# 1) SCHLUMBERGER TECHNOLOGY CORP.

# In[1]:


class method7():
    
    def __init__(self):
        self.regex =  re.compile(r'\d{2}-\d{3}-\d{5}') #catching API number
        return
    
    def main(self,filename):
        text = extract_text(filename,page_numbers = [0])
        
        lines = []
        
        for line in text.split('\n'):
            lines.append(line)
            
        count = 0
        
        for line in lines:
            
            count += 1
            
            match = self.regex.search(line)
            
            if match != None:
                
                
                
                rig_name =  lines[count-3]
                
                return rig_name
            
            


# In[ ]:





# ## Method 8
# 1) HALLIBURTON ENERGY SERVICES

# In[2]:


class method8():
    
    def __init__(self):
        self.regex =  re.compile(r'\d{2}-\d{3}-\d{5}') #catching API number
        self.regex2 = re.compile(r'API#') 
        return
    
    def main(self,filename):
        text = extract_text(filename,page_numbers = [0])
        
        
        lines = []
        
        for line in text.split('\n'):
            lines.append(line)
            
        count = 0
        
        for line in lines:
            
            count += 1
            
            match = self.regex.search(line)
            
            if match != None:
                
#                 print(match.group(0))
                
                rig_name =  lines[count-2]
                
                if rig_name == '':
                    text2 = extract_text(filename,page_numbers = [1])
                    
                    lines2 = []
                    
                    for line in text2.split('\n'):
                        lines2.append(line)
                    
                    count2 = 0
#                     print(lines2)
                    
                    for line in lines2:
                        
                        count2 += 1
                        
                        match2 = self.regex2.search(line)
                        
                        if match2 != None:
                            
                            rig_name = lines2[count2-2]
#                             print(match2.group(0))
                            
                            return rig_name    
                        
                else:
                
                    return rig_name


# ## Method 9
# 
# 1) TRUE SHOT, LLC

# In[ ]:


class method9():
    
    def __init__(self):
        self.regex =  re.compile(r'Rig:\s+\w+.*')
        return
    
    def main(self,filename):
        text = extract_text(filename,page_numbers = [0])
        
        for line in text.split('\n'):
            
            match = self.regex.search(line)
            
            if match != None:
                
                rig_name =  match.group(0).replace('Rig:','').strip()
                
                return rig_name
            


# ## Method 10
# 1) BAKER HUGHES INTEQ

# In[11]:


class method10():
    
    def __init__(self):
        self.regex =  re.compile(r'.*B\)')
        return
    
    def main(self,filename):
        text = extract_text(filename,page_numbers = [0])
        
        for line in text.split('\n'):
            
            match = self.regex.search(line)
            
            if match != None:
                
                rig_name =  match.group(0).split('(')[0].strip()
                
                if rig_name.find('Rig:') != -1:
                    rig_name = rig_name.strip('Rig:').strip()
                    
                if rig_name.find('referenced to') != -1:
                    rig_name = rig_name.split('to')[1].strip()
                
                return rig_name


# In[59]:


# m = method10()
# name = m.main('dir_survey_5151832.pdf')
# name


# ## Method 11
# 1) INVICTUS TOOLS, LLC

# In[61]:


class method11():
    
    def __init__(self):
        self.regex =  re.compile(r'Job Notes:') #catching API number
        return
    
    def main(self,filename):
        text = extract_text(filename,page_numbers = [0])
        
        lines = []
        
        for line in text.split('\n'):
            lines.append(line)
            
        count = 0
        
        for line in lines:
            
            count += 1
            
            match = self.regex.search(line)
            
            if match != None:
                
                
                
                rig_name =  lines[count+1]
                
                return rig_name
            


# In[1]:


# m = method11()
# name = m.main('dir_survey_5160054.pdf')
# name


# In[ ]:





# In[ ]:




