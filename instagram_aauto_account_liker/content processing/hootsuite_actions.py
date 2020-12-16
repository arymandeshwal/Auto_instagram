#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path
import os
import random
from shutil import copy2
#import Collections


# In[2]:


class Hootsuite:
    def __init__(self):
        ChromeOptions = webdriver.ChromeOptions()
        #ChromeOptions.headless = True
        userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        ChromeOptions.add_argument(f'user-agent={userAgent}')
        self.bot = webdriver.Chrome(options = ChromeOptions)
    
    def login(self,username,password):
        bot = self.bot
        bot.get("https://hootsuite.com/login")
        time.sleep(5)
        l_username = bot.find_element_by_id("loginEmailInput")
        l_password = bot.find_element_by_id("loginPasswordInput")
        l_username.send_keys(username)
        l_password.send_keys(password)
        l_password.send_keys(Keys.RETURN)
        time.sleep(5)
        #print(bot.current_url)
        print("Logged IN")
    
    def create_post(self):
        bot = self.bot
        #bot.find_element_by_class_name("vk-NewPostButton.sc-ezYOhE.eCQgiZ").click()
        bot.find_element_by_xpath('//*[@id="globalNavigation"]/div/div[1]/div[1]/div[1]/div[3]/div[1]/button/div/div').click()
        time.sleep(10)
        print("Created Post")
        
        #bot.find_element_by_class_name("_mediaUploadDropzoneClickArea.dz-clickable").click()
    
    def send_post_details(self,path,title):
        bot = self.bot
        bot.find_element_by_class_name("public-DraftStyleDefault-block.public-DraftStyleDefault-ltr").send_keys(title+"\n\n\n\n#dog #dogsofinstagram #dogs #dogstagram #doglover #dogoftheday #instadog #doglovers #doglife #dogsofinsta #cat #catsofinstagram #cateringjakarta #catnip #catsoftoronto #catgirls #baby #babygirl #babyhamper #babyaccessories #babycloth #babyfeeding #plant #plants #planter #plantparenthood #plantgeek #plantsofinstagram #cute #love")
        time.sleep(1)
        file = bot.find_element_by_class_name("dz-hidden-input")
        file.send_keys(path)
        time.sleep(60)
        bot.find_element_by_xpath('//*[@id="fullScreenComposerMountPoint"]/div/div/div/div/div/div[3]/div[3]/button').click()
        time.sleep(2)
        try:
            temp = bot.find_element_by_class_name("sc-fTIFLe.bveMJK").text
            print("box length ====> {}".format(len(temp)))
            if len(temp) == 65:
                print("Posted successfully!")
                return "Posted"
            else:
                print("THERE WAS AN ERROR WHILE POSTING")
        except Exception as e:
            print("Posted successfully!")
            print(e)
            return "Posted"
        return "Error"
    def quit(self):
        bot = self.bot
        bot.close()
        bot.quit()


# In[3]:


#Starting the code
h = Hootsuite()
h.login("","")
h.create_post()
#h.send_post_details(path)


# In[18]:


# Getting file path and title
folder = random.choices(["videos_converted","images_converted"])[0]
path = r"D:\d_folders\personal_projects\instagram_aauto_account_liker\content processing\content\{}\\".format(folder)
print(folder)
files = os.listdir(path)
if len(files) < 2:
    print("NEED TO DOWNLOAD SOME CONTENT")
title = files[0]
title = '.'.join(title.split(".")[:-1])
file_path = path[:-1]+files[0]
file_path,title
print("Got file path and file title.")


# In[5]:


# post output should be "posted"
result = h.send_post_details(file_path,title)
h.quit()


# In[19]:


# Copy and remove posted files
ext = file_path.split(".")[-1]
ext = "."+ext
#result = "posted"
if result == "Posted":
    dst = r"D:\d_folders\personal_projects\instagram_aauto_account_liker\content processing\content\posted\{}".format(title+ext)
    src = file_path
    copy2(src,dst)
    print("COPYING => {} to {}".format(title+ext, dst))
    os.remove(file_path)
    print("DELETING => {} from {}".format(title+ext,file_path))
    org_path = r"D:\d_folders\personal_projects\instagram_aauto_account_liker\content processing\content\{}\\".format(str(folder.split('_')[0]))
    print(org_path[:-1])
    for i in os.listdir(org_path):
        temp = ".".join(i.split('.')[:-1])
        if title == temp:
            final_path = org_path[:-1]+i 
            os.remove(final_path)
            print("DELETING => {} from {}".format(i,final_path))


# In[ ]:




