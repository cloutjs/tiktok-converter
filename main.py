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
    browser.get('https://vm.tiktok.com/ZMdF6u9A4/')
    url = browser.current_url
    browser.quit()
    cls()
    print("New URL:\n")
    print(url)
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

