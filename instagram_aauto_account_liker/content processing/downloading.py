from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from  pathlib import Path 
from aspect_ratio_change import *


class Download():
    def __init__(self):
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.headless = True
        #ChromeOptions.add_argument('--headless')
        #ChromeOptions.add_argument('--disable-gpu')
        self.data = Path("D:/d_folders/personal_projects/instagram_aauto_account_liker/content processing/content/videos")
        prefs = {"download.default_directory":r"D:\d_folders\personal_projects\instagram_aauto_account_liker\content processing\content\videos\\"}
        ChromeOptions.add_experimental_option("prefs",prefs)
        self.bot = webdriver.Chrome(options = ChromeOptions)
        #self.bot.get("https://lew.la/reddit/")

    def video(self,url):
        bot = self.bot
        bot.get("https://lew.la/reddit/")
        time.sleep(3)
        link = bot.find_element_by_id("video-url-input")
        link.send_keys(url)
        bot.find_element_by_class_name("get-video-button").click()
        time.sleep(5)
        try:
            bot.find_elements_by_class_name("save-button")[-1].click()
        except Exception as e:
            print("ERROR")
            print(e)

    def quit(self):
        bot = self.bot
        bot.close()
        bot.quit()

    def image(self,url):
        url = url+".json"
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        response = requests.get(url,headers={'User-agent': useragent})
        print(response)
        if not response.ok:
            print("Trying again!!")
            time.sleep(5)
            response = requests.get(url,headers={'User-agent': useragent})
            print(response)
            if not resposne.ok:
                print("ERROR")
                exit()
        data = response.json()
        #print(data)
        
        title = data[0]["data"]["children"][0]["data"]["title"]
        link = data[0]["data"]["children"][0]["data"]["url"]
        title = title.strip()
        title = title.replace('"',"")
        title = title.replace("'","")
        image = requests.get(link,headers={'User-agent': useragent})
        extension = link.split(".")[-1]
        name = title+"."+extension
        print("Saved as:\t{}".format(name))
        if image.status_code == 200:
            try:
                output_filehandle = open("D:/d_folders/personal_projects/instagram_aauto_account_liker/content processing/content/images/"+name,mode= "bx")
                output_filehandle.write(image.content)
            except Exception as e :
                print(e)

s = Download()
print("To exit the program put URL = 911")
while True:
    url = input("Enter the URL:\t")
    if url == "911":
        s.quit()
        break
    choice  = int(input("Is it a video or an Image?\nEnter [1] for video and [2] for image:\t"))
    if choice ==1:
        s.video(url)
    else:
        s.image(url)
print("--------------CHANGING ASPECT RATIOS AND FILE SIZE---------------------")
main()
exit()
