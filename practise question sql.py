#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as conn
mydb = conn.connect(host = 'localhost', user = 'root', passwd = 'arshad1234')
cursor = mydb.cursor()


# In[5]:


cursor.execute("create database cardataset")


# In[6]:


cursor.execute("create table cardataset.car1 (COL1 VARCHAR(20), COL2 VARCHAR(20), COL3 VARCHAR(10), COL4 VARCHAR(20),COL5 VARCHAR(20), COL6 VARCHAR(20), COL7 VARCHAR(20))")


# In[16]:


import csv
with open('car.data', 'r') as f :
    car_data = csv.reader(f, delimiter = '\n')
    print(car_data)
    query = """insert into cardataset.car1(COL1,COL2,COL3,COL4,COL5,COL6,COL7) values (%s,%s,%s,%s,%s,%s,%s)"""
    for i in car_data:
        split = str(i[0]).split(",")
        
        
        cursor.execute(query, split)
mydb.commit()        


# In[3]:


cursor.execute("select * from cardataset.car1")
cursor.fetchall()


# In[6]:


cursor.execute("select count(COL1) from cardataset.car1 group by COL1") #using group by function
cursor.fetchall()


# In[2]:


cursor.execute("select * from cardataset.car1 where col3 = 4") # filtering out col3 values which is equal to 4
cursor.fetchall()


# In[10]:


cursor.execute("update cardataset.car1 set COL3 = '8' where COL3 = '2'") #updating col3 values with 8 if its value is 2


# In[11]:


cursor.execute("select * from cardataset.car1")


# In[12]:


cursor.fetchall()


# In[13]:


mydb.commit()


# In[15]:


cursor.execute("set sql_safe_updates = 0")
cursor.execute("delete from cardataset.car1") # deleting car table


# In[16]:


cursor.execute("set sql_safe_updates = 1")
cursor.execute("select * from cardataset.car1")
cursor.fetchall()


# In[ ]:




