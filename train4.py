import pytest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    service=Service(r"C:\Users\HP\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    options= webdriver.ChromeOptions()
    drive=webdriver.Chrome(service=service, options=options)
    drive.maximize_window()
    drive.get("https://lambdatest.github.io/sample-todo-app/")
    try:
        li1=WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.NAME, 'li1')))
        li1.click()
        li2= WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.NAME, 'li2')))
        li2.click()
        title= 'Sample page - lambdatest.com'
        assert title == drive.title
        sample_text="Happy Testing at Lambdatest"
        email= WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.ID , 'sampletodotext')))
        email.send_keys("brahim.ezzyouy@gmail.com")
        email.click()
        sleep(5)
        addbutton=WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.ID, 'addbutton')))
        addbutton.click()
        sleep(5)
        sleep(20)
        drive.quit()
    except TimeoutException:
        print('Element not found')
    sleep(10)
    drive.quit()