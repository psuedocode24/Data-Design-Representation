#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:19:12 2022

@author: ashimalik
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Part 1 ('Askew')

# Installing the latest ChromeDriver using Driver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#driver.implicitly_wait(10)
#driver.set_script_timeout(120)
#driver.set_page_load_timeout(10)

driver.get("https://www.bestbuy.com");
time.sleep(10)

# Checking for the annoying pop-up
try:
    popup = driver.find_element_by_css_selector("button[aria-label='Close']")
    popup.click()
    time.sleep(2)
except:
    print("Test")
    pass

deal = driver.find_element_by_xpath("//a[text()='Deal of the Day']")

deal.click()
time.sleep(5)
hours = driver.find_element_by_css_selector("span[class= 'hours cdnumber']").text
minutes = driver.find_element_by_css_selector("span[class= 'minutes cdnumber']").text
seconds = driver.find_element_by_css_selector("span[class= 'seconds cdnumber']").text
time.sleep(10)
product = driver.find_element_by_css_selector("h1[class = 'heading product-title']")
product.click()
time.sleep(5)


reviews = driver.find_element_by_css_selector("span[class = 'c-reviews-v4 c-reviews order-2']")
reviews.click()
time.sleep(5)

def saveString(html, filename="text.html"):
	try:
		file = open(filename,"w")
		file.write(str(html))
		file.close()
	except Exception as ex:
		print('Error: ' + str(ex))
saveString(driver.page_source, 'bestbuy_deal_of_the_day.html')  



print("Time is: {}:{}:{}".format(hours,minutes,seconds))
driver.quit()