#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlalchemy


# In[27]:


class pushRigs():
    
    def __init__(self):
        self.engine = sqlalchemy.create_engine("postgresql://rigextract:G1bson!@railroad-prod.cxmxeomzvjpa.us-east-2.rds.amazonaws.com:5432/postgres")
        self.conn = self.engine.connect()
#         print(self.engine.table_names())
        return
        
    def push(self,rigTable):
        
        rigTable['externalattachmentid'] = rigTable['externalattachmentid'].astype(str)
        
        tableName = 'rigextract'
        
        currentTable = pd.read_sql_table('rigextract',self.engine,schema = 'railroad', columns = ['externalattachmentid','rigname'])
        
        #Check and find new ids
        currentIds = list(currentTable['externalattachmentid'])
        newIds = list(rigTable['externalattachmentid'])
        newUniqueIds = list(set(newIds) -  set(currentIds))
        
        newRecords = rigTable[rigTable['externalattachmentid'].isin(newUniqueIds)]
    
        
#         newRecords = rigTable.merge(currentTable,how = 'left', indicator = True).loc[lambda x: x['_merge'] == 'left_only']
#         newRecords = newRecords.drop(columns = ['_merge'])

        print(newRecords)
        
        
#         newRecords.to_sql(tableName, self.conn.execution_options(autocommit = True), schema = 'railroad', if_exists = 'append',index = False)
        
        self.conn.close()
        return
        
    


# In[28]:





# In[1]:





# In[ ]:





# In[ ]:




