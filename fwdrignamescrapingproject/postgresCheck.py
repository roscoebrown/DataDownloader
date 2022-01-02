#!/usr/bin/env python
# coding: utf-8

# In[2]:


import psycopg2 as ppg


# In[4]:


class postgresCheck():
    
    def __init__(self):
        self.conn = ppg.connect(
        database = 'postgres',
        user = 'rigextract',
        password = 'G1bson!',
        host = 'railroad-prod.cxmxeomzvjpa.us-east-2.rds.amazonaws.com',
        port = '5432')
        
        self.cur1 = self.conn.cursor()
        self.cur2 = self.conn.cursor()
        
    def checkFile(self,filename):
        survey_id = filename.split('.')[0].split('_')[2]
        EAID = "'" + survey_id +"'"
        SQL = """
        SELECT externalattachmentid,surveycompany,surveytype 
        FROM railroad.completesurveydata 
        WHERE externalattachmentid = {}
        """.format(EAID)
        
        self.cur1.execute(SQL)
        self.cur2.execute(SQL)
        
        if len(self.cur1.fetchall()) != 0:
            for record in self.cur2.fetchall():
                EAID, surveyCompany, surveyType = record
                return [surveyCompany,surveyType]
        else:
            return 'missing'
        
    def checkRig(self,filename):
        survey_id = filename.split('.')[0].split('_')[2]
        EAID = "'" + survey_id +"'"
        SQL = """
        SELECT externalattachmentid
        FROM railroad.rigextract
        WHERE externalattachmentid = {}
        """.format(EAID)
        
        self.cur1.execute(SQL)
        
        if len(self.cur1.fetchall()) != 0:
            return 'rig already extracted'
        else:
            return 'missing'
        
        
        


# In[ ]:




