# TSSPython_144350004
In the week 5 assignment, I have used Selenium for downloading data from Ministry of Health and Family Welfare website https://hmis.nhp.gov.in/#!/standardReports. The website has many folders nested inside one another and the files are stored as excel or pdf.
to download the files i have to nagivate through the folders back and forth.
For this assignment, the following modules are used

from selenium import webdriver 

from selenium.webdriver.common.by import By 

from selenium.webdriver.support.ui import WebDriverWait 

from selenium.webdriver.support import expected_conditions as EC 

import time

webdriver module is used for setting up the webdriver and optional settings for opening the webpage. Chrome is used for this assignment
The compatible driver for chrome is downloaded from https://sites.google.com/a/chromium.org/chromedriver/downloads, and stored in a location on the computer. 

The PATH where the driver is stored in my pc is r"D:\webdriver\bin\chromedriver.exe"
is called into the driver = webdriver.Chrome(PATH) function.

options = webdriver.ChromeOptions() is used for changing path for downloading the data, and also for triggering errors due t ossl and certificate (if needed)

the options are passed into webdriver.Chrome(PATH, options=options)

The elements in the webpage are identified through inspect element, the XPATH of the elements are used in the code to navigate through the webpage.
WebDriverWait is used for explicit wait till the element is found in the webpage 

expected_conditions as EC is used for searching the element located by XPATH and called in By.XPATH

The syntax commonly for executing the path and navigating is 

try:

  element = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"path"))).click()
  
except:

  time.sleep(5)
  
  driver.close()
  
 the time module is used to set the sleep time before the driver.close() closes the browser
 
 The code is used for downloading few sample files in folder using for loop and navigating back and forth to download files from different folders.
 

