from selenium import webdriver
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def convert():
    cls()
    print("Converting...")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.get(vid)
    url = browser.current_url
    browser.quit()
    cls()
    e = url.split(".html")
    print("New URL:\n")
    print(e[0])
    time.sleep(5)

def botting():
    cls()
    print("Success")
    time.sleep(5)

vid = input("TikTok URL: ")
if vid.startswith("https://vm"):
    convert()
elif vid.startswith("vm."):
    convert()
else:
    botting() 




