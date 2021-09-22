#!/usr/bin/env python
# coding: utf-8



#                               for rotating over dates stage-1
import datetime
dates=[]
start = datetime.datetime.strptime("2011-01-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2011-01-2", "%Y-%m-%d")
date_array =     (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
for date_object in date_array:
    dates.append(date_object.strftime("%d-%b-%Y"))
# print(len(dates))   for counting number of dates 
#                                        stage-2

# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import pandas as pd

# url for scrapping
url = "https://bsestarmf.in/RptNavMaster.aspx"   
# crome driver for opening website
chromeOptions = webdriver.ChromeOptions()
# for storing the files in the local machine 
prefs = {"download.default_directory" : "E:\newdata"}
chromeOptions.add_experimental_option("prefs",prefs)
# localtion of crome driver in local machine
chromedriver = r"C:\Users\rahul\.wdm\drivers\chromedriver\win32\92.0.4515.107\chromedriver"
# running the script and storing the path at the given location
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
driver.get(url)
# commands for processing the given task
# for every element the element id is been used 
for i in dates:
    dataa=driver.find_element_by_id("txtToDate").clear()
    dataa=driver.find_element_by_id("txtToDate").send_keys(i)
    dataa=driver.find_element_by_id("txtToDate").click()
    down_data=driver.find_element_by_id('btnText').click()

# quitting the process after completing the task 
driver.quit()








