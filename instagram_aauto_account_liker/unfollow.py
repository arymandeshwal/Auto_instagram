#!/usr/bin/env python
# coding: utf-8

# In[1]:


from instapy import InstaPy


# In[2]:


session = InstaPy(username="", password="")


# In[3]:


session.login()


# In[4]:


dir(session)


# In[5]:


usernames = session.grab_following(username="_fifty_shades_of_us_", amount="full")


# In[6]:


print(usernames)


# In[7]:


import inspect


# In[8]:


print(inspect.getfullargspec(session.unfollow_users))


# In[ ]:


session.unfollow_users(amount = len(usernames),custom_list_enabled=True,custom_list = usernames,allFollowing = True)


# In[ ]:




