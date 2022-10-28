#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install mysql-connector-python')


# In[1]:


import mysql.connector as arshad


# In[2]:


mydb = arshad.connect(host = 'localhost', user = 'root', passwd = "arshad1234")


# In[3]:


mydb


# In[4]:


cursor = mydb.cursor()


# In[5]:


cursor.execute("show databases")


# In[6]:


cursor.fetchall()


# In[17]:


cursor = mydb.cursor()


# In[18]:


cursor.execute("create database test")


# In[23]:


cursor.execute("create table test.player(player_id INT(10), player_name VARCHAR(30), lastname VARCHAR(30), player_ht INT(10))")


# In[7]:


cursor.execute('use test')


# In[8]:


cursor.execute('show tables')


# In[9]:


cursor.fetchall()


# In[12]:


cursor.execute("insert into test.player values(123, 'Messi', 'Leo', 5.5)")


# In[13]:


mydb.commit()


# In[14]:


cursor.execute("select * from test.player")


# In[16]:


cursor.fetchall()


# In[21]:


cursor.execute("insert into test.player values(124, 'ronaldo', 'Leo', 5)")


# In[22]:


mydb.commit()


# In[8]:


cursor.execute("select * from test.player")


# In[9]:


cursor.fetchall()


# In[10]:


cursor.execute("create table test.glassdata(col1 INT(10), col2 float(10,5), col3 float(10,5), col4 float(10,5), col5 float(10,5), col6 float(10,5), col7 float(10,5), col8 float(10,5), col9 float(10,5), col10 float(10,5), col11 INT(10))")


# In[14]:


cursor.execute('use test')


# In[15]:


cursor.execute('show tables')


# In[16]:


cursor.fetchall()


# In[7]:


f = open('glass.data', 'r+')


# In[8]:


f.read()


# In[9]:


import csv
with open('glass.data', 'r') as f:
    glass_data = csv.reader(f, delimiter = '\n')
    for i in glass_data:
        print(i[0])


# In[10]:


cursor.execute("create table test.glassdata(col1 INT(10), col2 float(10,5), col3 float(10,5), col4 float(10,5), col5 float(10,5), col6 float(10,5), col7 float(10,5), col8 float(10,5), col9 float(10,5), col10 float(10,5), col11 INT(10))")


# In[ ]:


cursor.execute("insert into test.glassdata values(1,1.52101,13.64,4.49,1.10,71.78,0.06,8.75,0.00,0.00,1)")


# In[ ]:


mydb.commit()


# In[ ]:


cursor.execute('select * from test.glassdata')


# In[ ]:


cursor.fetchall()


# In[13]:


import csv
with open('glass.data', 'r') as f:
    glass_data = csv.reader(f, delimiter = '\n')
    for i in glass_data:
        print(i)
        print(f'insert into glassdata values ({str(i[0])})')
        cursor.execute(f'insert into test.glassdata values ({str(i[0])})')


# In[14]:


mydb.commit()


# In[15]:


import pandas as pd


# In[16]:


pd.read_sql('show databases', mydb)


# In[ ]:





# In[ ]:




