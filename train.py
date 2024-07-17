from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep

service=Service(r"C:\Users\HP\Downloads\edgedriver_win64\msedgedriver.exe")
options=webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)
driver.get("https://www.linkedin.com/pulse/selenium-un-guide-exhaustif-pour-lautomatisation-des-tests-barta/")
sleep(10) 
driver.quit()

 