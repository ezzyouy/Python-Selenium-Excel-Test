from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service


if __name__== '__main__':
    service=Service(r"C:\Users\HP\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    options=webdriver.ChromeOptions()
    drive=webdriver.Chrome(service=service, options=options)
    drive.maximize_window()
    drive.get('https://accounts.lambdatest.com/login?_gl=1*kscq4z*_gcl_au*MTA2ODc1OTI4Ny4xNjk1NzMyOTM3')
    try:
        myElem_1=WebDriverWait(drive,10).until(EC.presence_of_element_located((By.ID,'email')))
        myElem_1.send_keys("brahim.ezzyouy@gmail.com")
        myElem_1.click()
        myElem_2=WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.ID, 'password')))
        myElem_2.send_keys("Password1@")
        myElem_2.click()
        myElem_3=WebDriverWait(drive, 10).until(EC.presence_of_element_located((By.ID, 'login_button')))
        myElem_3.click()
        sleep(10)
    except:
        print("No element found")
    sleep(10)
    drive.close()
