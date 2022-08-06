#!/usr/bin/env python
# coding: utf-8

# In[2]:


import psycopg2
import pandas as pd

#connecting to the database
conn = psycopg2.connect(database = 'database',
                        user =     'user',
                        password = 'password',
                        host =     'host',
                        port =     'port')

#creating a connection object
cur = conn.cursor()

#created the table
#cur.execute("""CREATE TABLE justdb( CVE INT PRIMARY KEY, justifications text)""")
cur.execute("""CREATE TABLE JustificationsDB (CVE Char(50) Primary Key, justifications text)""")
conn.commit()


# In[69]:


#altering table type
x = """ALTER TABLE justdb ALTER COLUMN cve TYPE Char(50)"""
cur.execute(x)


# In[2]:


#inserting data into the table
postgres_insert_query = """ INSERT INTO justdb VALUES ('CVE-2021-35937', 'Inherited from base image.')"""
cur.execute(postgres_insert_query)
conn.commit()


# In[3]:


sql = """ SELECT * from JustificationsDB """
pd.read_sql(sql, con=conn)


# In[ ]:




