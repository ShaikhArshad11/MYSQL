#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as arshad


# In[2]:


mydb = arshad.connect(host = 'localhost', user = 'root', passwd = 'arshad1234')


# In[3]:


cursor = mydb.cursor()


# In[4]:


cursor.execute('show databases')


# In[5]:


cursor.fetchall()


# In[6]:


cursor.execute('select * from test.glassdata')


# In[7]:


cursor.fetchall()


# In[54]:


cursor.execute('select * from test.player')


# In[11]:


cursor.fetchall()


# In[12]:


cursor.execute('select col1, col5, col10 from test.glassdata')
cursor.fetchall()


# In[18]:


cursor.execute('select * from test.glassdata where col1 = 4 and col11 = 1')
cursor.fetchall()


# In[24]:


cursor.execute('delete from test.glassdata where col1 = 4 and col11 = 1')


# In[23]:


mydb.commit()


# In[8]:


cursor.execute('select * from test.glassdata where col1 = 4 and col11 = 1')
cursor.fetchall()


# # GROUP BY OPERATION IN SQL

# In[14]:


cursor.execute('select count(col1), col2 from test.glassdata group by col1')
cursor.fetchall()


# In[21]:


cursor.execute('select col1, count(col1) from test.glassdata group by col1 order by col1')
cursor.fetchall()


# In[27]:


cursor.execute("select count(*), player_name from test.player where lastname = 'Leo'")
cursor.fetchall()


# In[28]:


cursor.execute("drop table test.player")
mydb.commit()


# In[34]:


cursor.execute("alter table test.glassdata drop column col11")
cursor.fetchall()


# In[35]:


cursor.execute("select * from test.glassdata")
cursor.fetchall()


# In[9]:


cursor.execute("select col1, col8 from test.glassdata where col1 = 11 or col8 = 2")
cursor.fetchall()


# In[10]:


cursor.execute("select * from test.glassdata where col2 like '1.515%'")
cursor.fetchall()


# In[8]:


cursor.execute("select * from test.glassdata")
cursor.fetchall()


# In[10]:


cursor.execute("select * from test.glassdata order by col2") # order it in ascending order of col2
cursor.fetchall()


# In[11]:


cursor.execute("select * from test.glassdata order by col2 desc") # order it in descending order of col2
cursor.fetchall()


# In[9]:


cursor.execute("select * from (select * from test.glassdata where col1 > 112) as shit where col6 = 70.57")
cursor.fetchall()


# In[10]:


cursor.execute("select * from (select * from test.glassdata where col1 > 112) as shit where col8 = 12")
cursor.fetchall()


# In[11]:


cursor.execute("select * from test.glassdata")
cursor.fetchall()


# In[16]:


cursor.execute("select * from test.glassdata group by col1 having count(col1) > 2")
cursor.fetchall()


# In[19]:


f = open("car.data", 'r+')
f.read()


# In[10]:


import csv 
with open("car.data", "r") as f:
    car_data = csv.reader(f, delimiter = '\n')
    for i in car_data:
        print(i[0])


# In[11]:


cursor.execute("create table test.cardataset (vhigh VARCHAR(20),vhigh VARCHAR(20),2 INT(10),2 INT(10),small VARCHAR(20),low VARCHAR(20),unacc VARCHAR(20))")


# In[32]:


cursor.fetchall()


# In[15]:


import csv
with open('car.data', 'r') as f :
    car_data = csv.reader(f, delimiter = '\n')
    for i in car_data:
        print(i)


# In[ ]:




