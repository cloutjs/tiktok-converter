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
    print("New URL:\n")
    print(url)
    time.sleep(15)

def success():
    cls()
    print("Already a normal URL or not a URL at all.")
    time.sleep(15)

vid = input("TikTok URL: ")
if vid.startswith("https://vm"):
    convert()
elif vid.startswith("vm."):
    convert()
else:
    success()


