from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


service= Service  
options=webdriver.ChromeOptions()
drive=webdriver.Chrome(options=options, service=service)
drive.get("https://www.jumia.ma/")

sleep(10)
drive.quit()