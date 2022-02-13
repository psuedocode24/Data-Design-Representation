#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 18:46:41 2022

@author: ashimalik
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Part 1 ('Askew')

# Installing the latest ChromeDriver using Driver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.set_script_timeout(120)
driver.set_page_load_timeout(10)

driver.get("https://google.com");
inp = driver.find_element_by_css_selector("input[type=text]")
inp.send_keys("Askew\n")
time.sleep(10)
driver.quit()


