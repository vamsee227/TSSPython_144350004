from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import os

import time

download_path = r"E:\coding\python\Week-5"

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--ignore-ssl-errors=yes')
options_chrome.add_argument('--ignore-certificate-errors')
pref_folder = {"download.default_directory": download_path}
options_chrome.add_experimental_option("prefs", pref_folder)

PATH = r"D:\webdriver\bin\chromedriver.exe"
driver = webdriver.Chrome(PATH, options = options_chrome)
driver.get("https://hmis.nhp.gov.in/#!/standardReports")
print(driver.title)

def back():
        back = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[1]/div[2]/input'))
    ).click()


try:
    folder1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/img'))
    ).click()

    folder2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/img'))
    ).click()
     
    folder3 = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[2]/table[1]/tbody/tr[2]/td[1]/img'))
    ).click()

    folder4 = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/img'))
    ).click()
    
    
    for i in range(2,5):
        file_path = "/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[" +str(i)+"]/td[1]/a/img"
        files = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(
                (By.XPATH, file_path))
        ).click()   

    back()
    folder6 = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[1]/img'))
    ).click()

    for i in range(2,5):
        file_path = "/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[" +str(i)+"]/td[1]/a/img"
        files = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(
                (By.XPATH, file_path))
        ).click()   

    back()
    back()    

    folder7 = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[2]/table[1]/tbody/tr[3]/td[1]/img'))
    ).click()

    folder8 = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/img'))
    ).click()
    for i in range(2,4):
        file_path = "/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[" +str(i)+"]/td[1]/a/img"
        files = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(
                (By.XPATH, file_path))
        ).click() 
    back()
    
    folder9 = WebDriverWait(driver,20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[1]/img'))
    ).click()    

    for i in range(2,4):
        file_path = "/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tbody/tr[" +str(i)+"]/td[1]/a/img"
        files = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(
                (By.XPATH, file_path))
        ).click()

    back()
    back()   

    for i in range(2,5):
        file_path = "/html/body/div[2]/main/div/div/div[2]/div/div[2]/table[2]/tbody/tr[" +str(i)+"]/td[1]/a/img"
        zip_files = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(
                (By.XPATH, file_path))
        ).click()
    time.sleep(5)
    driver.close()

except:
    time.sleep(5)   
    driver.close()
