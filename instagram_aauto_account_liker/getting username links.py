#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os


# In[3]:


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        #notif_dialog = bot.find_element_by_class_name('aOOlW.HoLwm').click()
    
    def like(self,hashtag):
        bot = self.bot
        time.sleep(5)
        print("page switching")
        bot.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        time.sleep(2)
        
        username_links =[]
        
        all_links =[]
        for i in range(0,10):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(4)
            posts = bot.find_elements_by_class_name('v1Nh3.kIKUG._bz0w')
            links =[post.find_element_by_css_selector('a').get_attribute('href') for post in posts]
            for link in links:
                all_links.append(link)
        
        all_links = list(set(all_links))
        print(len(all_links))
        for link in all_links:
            bot.get(link)
            time.sleep(1)
            try:
                username_link = bot.find_element_by_class_name('sqdOP.yWX7d._8A5w5.ZIAjV').get_attribute("href")
                time.sleep(1)
                username_links.append(username_link)
            
            except Exception as ex:
                print(ex)
                time.sleep(10)
        return username_links


# In[4]:


usernmae,password,hashtag ='_fifty_shades_of_us_','Aryman9811605301','fitness'
ins = Instagram(usernmae,password)
ins.login()
username_links =[]
try:
    for i in ["throwback","nba","python","gym","disney","movies","csgo","fitness","food"]:
        temp = ins.like(i)
        for j in temp:
            username_links.append(j)
except:
    print("Error occured!")


# In[5]:


username_links = list(set(username_links))


# In[6]:


len(username_links)


# In[7]:


df = pd.read_csv("links.csv")
df.shape


# In[8]:


old_links = df.links.to_list()
print(len(old_links))


# In[9]:


total_links = old_links + username_links
print(len(total_links))
total_links = list(set(total_links))


# In[10]:


len(total_links)


# In[11]:


if os.path.exists("links.csv"):
    os.remove("links.csv")
df = pd.DataFrame({"links":total_links})
df.to_csv("links.csv",index=False)


# In[12]:


df.shape


# In[ ]:




