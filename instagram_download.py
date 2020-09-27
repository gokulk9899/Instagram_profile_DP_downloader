"""
Instagram profile pic Downloader using Python tkinter GUI
"""
#import neccessary files
import requests
import os
import json
import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
import shutil


#initializing Tkinter
insta = tk.Tk()
insta.title("Instagram Profile pic Downloader")
insta.geometry("600x400")

#Creating canvas
canvas = tk.Canvas(insta,height = 600,width = 400,bg = None)
bold_font = tkfont.Font(family = "Helvetica", size = 12,weight = "bold")

#Enter the Instagram Profile ID
label1 = tk.Label(insta,text = "Enter the Insta ID",width = 14,bg = None)
label1.config(font = bold_font)
canvas.create_window(100,50,window = label1)

#Get the Id using tkinter Entry
download_entry = tk.Entry(insta,width = 30,selectbackground='red')
canvas.create_window(270,50,window = download_entry)

#Enter the path where the profile_pic to be downloaded
label2 = tk.Label(insta,text = "Enter the Path",width = 10,bg = None)
label2.config(font = bold_font)
canvas.create_window(80,100,window = label2)

#Get the download path using tkinter Entry
path_entry = tk.Entry(insta,width = 30,selectbackground='red')
canvas.create_window(270,100,window = path_entry)

def browse_dir():
    save_path = filedialog.askdirectory()
    path_entry.delete(0)
    path_entry.insert(0,save_path)
    

#Browse button alternate to Entry text box for path 
browse = tk.Button(text= "Browse", padx=4,pady=2,fg = "white",bg = "blue",font = bold_font,command = browse_dir)
canvas.create_window(420,100,window=browse)

canvas.pack()

  
 
#Function invoked when GET button is clicked
def get_insta_dp():
    header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    }

    USER_ID = download_entry.get()
    save_path = path_entry.get()
    URL = "https://www.instagram.com/" + download_entry.get() + "/?__a=1"
    response = requests.get(URL, headers=header).json()
    hd_image_path = response["graphql"]["user"]["profile_pic_url_hd"]
    hd_image_response = requests.get(hd_image_path, stream=True)
    os.chdir(save_path)
    file_name= USER_ID + "_hd_img.jpg"
    with open(file_name, "wb") as out_file:
        shutil.copyfileobj(hd_image_response.raw, out_file)
    
    messagebox.showinfo("showinfo", "Profile Download Successfull!")#To notify that profile pic is downloaded

#GET button to download the profile pic 
download = tk.Button(text= "GET", padx=5,pady=5,fg = "white",bg = "#0000FF",font = bold_font,command = get_insta_dp)
canvas.create_window(300,150,window = download)

#Tkinter mainloop
insta.mainloop()


#End of the code






