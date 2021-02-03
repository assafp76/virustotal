#!/usr/bin/env python
# coding: utf-8

# In[192]:


get_results(get_response(get_scan_id("www.elementor.com"),"www.elementor.com"))


# In[189]:


get_scan_id("www.elementor.com")


# In[182]:


get_categories("www.elementor.com")


# In[195]:


import csv
import requests
reader = csv.reader(open(r'C:\Users\user\Downloads\request1.csv'))
for row in reader:
    print(f'"{row[0]}"')
    #scan_id = get_scan_id(f'"{row[0]}"')


# In[107]:


def get_scan_id(url):
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': 'c3c075812b29b698dbd8933241e675acd81df6ca132a8f6805627c30613441d7', 'url':url}
    response = requests.post(url, data=params)
    return response.json()['permalink'].split('detection/')[1]


# In[190]:


def get_response(scan_id,url):
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': 'c3c075812b29b698dbd8933241e675acd81df6ca132a8f6805627c30613441d7', 'resource':url,'scan_id':scan_id}
    response = requests.get(url, params=params)
    return(response.json())


# In[187]:


def get_results(response):
    clean = 0
    unrated = 0 
    malicious = 0
    phishing = 0
    malware = 0 
    for i in response['scans'].values():
        if i['result'] == 'clean site':
            clean = clean +1
        if i['result'] == 'unrated site':
            unrated = unrated +1
        if i['result'] == 'malicious site':
            malicious = malicious + 1
        if i['result'] == 'phishing site':
            phishing = phishing + 1
        if i['result'] == 'malware site':
            malware = malware + 1
    return('clean:'+str(clean),'unrated:'+str(unrated),'malicious:'+str(malicious),'phishing:'+str(phishing),'malware:'+str(malware))


# In[181]:


def get_categories(domain):
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey':'c3c075812b29b698dbd8933241e675acd81df6ca132a8f6805627c30613441d7','domain':domain}
    response = requests.get(url, params=params)
    a = response.json()
    l = []
    for k,v in a.items():
        if 'category' in k :
            l.append(v)
    print(set(l))





import sqlite3
db = sqlite3.connect(':memory:')  # Using an in-memory database
cur = db.cursor()


# In[18]:


cur.execute('''CREATE TABLE IF NOT EXISTS Customer (
                id integer PRIMARY KEY,
                firstname varchar(255),
                lastname varchar(255) )''')
cur.execute('''CREATE TABLE IF NOT EXISTS Item (
                id integer PRIMARY KEY,
                title varchar(255),
                price decimal )''')
cur.execute('''CREATE TABLE IF NOT EXISTS BoughtItem (
                ordernumber integer PRIMARY KEY,
                customerid integer,
                itemid integer,
                price decimal,
                CONSTRAINT customerid
                    FOREIGN KEY (customerid) REFERENCES Customer(id),
                CONSTRAINT itemid
                    FOREIGN KEY (itemid) REFERENCES Item(id) )''')


# In[19]:


cur.execute('''INSERT INTO Customer(firstname, lastname)
               VALUES ('Bob', 'Adams'),
                      ('Amy', 'Smith'),
                      ('Rob', 'Bennet');''')
cur.execute('''INSERT INTO Item(title, price)
               VALUES ('USB', 10.2),
                      ('Mouse', 12.23),
                      ('Monitor', 199.99);''')
cur.execute('''INSERT INTO BoughtItem(customerid, itemid, price)
               VALUES (1, 1, 10.2),
                      (1, 2, 12.23),
                      (1, 3, 199.99),
                      (2, 3, 180.00),
                      (3, 2, 11.23);''') # Discounted price 


# In[20]:


cur.execute('''SELECT itemid, AVG(price) FROM BoughtItem GROUP BY itemid''')


# In[21]:


print(cur.fetchall())

