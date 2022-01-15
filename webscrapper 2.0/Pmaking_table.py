from msilib.schema import tables
from venv import create
from matplotlib.pyplot import table
from sklearn.metrics import consensus_score
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from sqlalchemy.sql.schema import MetaData, Table
from tableauhyperapi import TableName
from sqlalchemy import Column, Integer, String

#engine = db.create_engine('sqlite:///SQL_Alchemy\sample-data.sql', echo = True)
#engine = db.create_engine('sqlite:///SQL_Alchemy/census2000names.sqlite', echo = True)
engine = db.create_engine('sqlite:///:memory:', echo = True)
Base = declarative_base()
metadata = MetaData()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)
     
            
ed_user= User(name = 'ed', fullname = 'Ed Jones', nickname = 'edsnickname')
print(ed_user.name)


#Base.metadata.create_all(engine)

'''
connection = engine.connect()


emp = db.Table('emp', metadata,
              db.Column('Id', db.Integer()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('salary', db.Float(), default=100.0),
              db.Column('active', db.Boolean(), default=True)
              )
# create a new table
#metadata.create_all(engine) #Creates the table


# inserting data
query = db.insert(emp).values(Id=1, name='naveen', salary=60000.00, active=True) 
ResultProxy = connection.execute(query)

#Inserting many records at ones
query = db.insert(emp) 
values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
ResultProxy = connection.execute(query,values_list)

results = connection.execute(db.select([surnames])).fetchall()

df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df.head(7))
'''