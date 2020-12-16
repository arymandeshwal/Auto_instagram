import cv2
import os
from pathlib import Path
from fractions import Fraction as frac
from moviepy.editor import *

def correct_size(height,width):
    new_width ,new_height = 0,0
    if height <= width:
        new_height = height
        #5/9 * x = height
        #x = height*9/5
        x = height*(9/5)
        new_width = x*(4/9)
    else:
        new_width = width
        x = width*(9/4)
        new_height = x*(5/9)

    return new_width,new_height


def image_conv(path,org_path,title):
    img = cv2.imread(path)
    height, width = img.shape[:2]
##    new_width ,new_height = 0,0
##    if height >= width:
##        new_height = height
##        #5/9 * x = height
##        #x = height*9/5
##        x = height*(9/5)
##        new_width = x*(4/9)
##    else:
##        new_width = width
##        x = width*(9/4)
##        new_height = x*(5/9)
    new_width,new_height = correct_size(height,width)
    print("New ====> {}".format(frac(new_width/new_height).limit_denominator()))
    
    # resizing
    resized = cv2.resize(img,(int(new_width),int(new_height)),interpolation = cv2.INTER_AREA)
    new_path = org_path / "images_converted"
    title = ".".join(title.split('.')[:-1])
    title += ".png"
    new_path /= title
    print(new_path)

    #cv2.imshow(str(new_path),resized)
    cv2.imwrite(str(new_path),resized)
    size = (os.stat(new_path).st_size)/1000000
    print("Size ==> {}mb".format(size))
    if size > 4.9: 
        scale = size/4.9
        new_width /= scale
        new_height /= scale
        os.remove(new_path)
        resized = cv2.resize(img,(int(new_width),int(new_height)),interpolation = cv2.INTER_AREA)
        cv2.imwrite(str(new_path),resized)
        size = (os.stat(new_path).st_size)/1000000
        print("New Size ==> {}mb".format(size))


def video_conv(path,org_path,title):
    clip = VideoFileClip(path)
    #print(clip.w,clip.h)
    print("original duration: {}".format(clip.duration))
    if int(clip.duration) >= 60:
        clip = clip.subclip(0,59)
        print("New duration: {}".format(clip.duration))
    new_width,new_height = correct_size(clip.h,clip.w)
    print(new_width,new_height)
    clip.resize((new_width,new_height))
    new_path = org_path / "videos_converted"
    title = ".".join(title.split('.')[:-1])
    title += ".mp4"
    new_path /= title
    #print(new_path)
    clip.write_videofile(str(new_path),threads=4,preset ='medium' ,logger = None,audio_codec = "aac")
    print("----------------done------------------")
    

       
def main():
    org_path = Path("D:\d_folders\personal_projects\instagram_aauto_account_liker\content processing\content")
    """
    Image part!
    """
    img_path = org_path / "images"
    img_converted_path = org_path / "images_converted"
    img_already_converted = os.listdir(img_converted_path)
    img_filtered =[]
    for i in img_already_converted:
        temp = '.'.join(i.split('.')[:-1])
        img_filtered.append(temp)

    for i in os.listdir(img_path):
        temp = '.'.join(i.split('.')[:-1])
        if temp not in img_filtered:
            print("Not present -----------------"+i)
            path = str(img_path / i)
            #print(path)
            image_conv(path,org_path,i)
    
    """
    Video part!
    """
    
    vid_path = org_path / "videos"
    vid_converted_path = org_path / "videos_converted"
    vid_already_converted = os.listdir(vid_converted_path)
    vid_filtered =[]
    for i in vid_already_converted:
        temp = '.'.join(i.split('.')[:-1])
        vid_filtered.append(temp)
    for i in os.listdir(vid_path):
        temp = '.'.join(i.split('.')[:-1])
        if temp not in vid_filtered:
            path = str(vid_path / i)
            video_conv(path,org_path,i)
          
    
#main()   
