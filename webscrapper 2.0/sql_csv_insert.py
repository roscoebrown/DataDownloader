import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, MetaData, String, SmallInteger, inspect
import pandas as pd
import psycopg2 as pg
#load python script that batch loads pandas df to sql
from io import StringIO


engine = db.create_engine('sqlite:///census2000names.sqlite')
connection = engine.raw_connection()
Base = declarative_base()
cursor = connection.cursor()

def creat_db_schema(engine):
    Base.metadata.create_all(engine)

df =pd.Dataframe([1],[1])
#df is the dataframe containing an index and the columns "Event" and "Day"
#create Index column to use as primary key
df.reset_index(inplace=True)
df.rename(columns={'index':'Index'}, inplace =True)

#create the table but first drop if it already exists
command = '''DROP TABLE IF EXISTS localytics_app2;
CREATE TABLE localytics_app2
(
"Index" serial primary key,
"Event" text,
"Day" timestamp without time zone,
);'''
cursor.execute(command)
connection.commit()

#stream the data using 'to_csv' and StringIO(); then use sql's 'copy_from' function
output = StringIO()
#ignore the index
df.to_csv(output, sep='\t', header=False, index=False)
#jump to start of stream
output.seek(0)
contents = output.getvalue()
cur = connection.cursor()
#null values become ''
cur.copy_from(output, 'localytics_app2', null="")    
connection.commit()
cur.close()