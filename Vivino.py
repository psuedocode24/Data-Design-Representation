from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/Users/tarang/Downloads/chromedriver')
driver.implicitly_wait(10)
driver.set_script_timeout(120)
driver.set_page_load_timeout(10)

driver.get("https://www.vivino.com/");

#         driver.find_element_by_class_name("className");
#         driver.find_element_by_css_selector".className");
#         driver.find_element_by_id("elementId");
#         driver.find_element_by_link_text("linkText");
#         driver.find_element_by_name("elementName");
#         driver.find_element_by_partial_link_text("partialText");
#         driver.find_element_by_tag_name("elementTagName");
         

wines = driver.find_element_by_css_selector("span[title='Wines']")
wines.click()
time.sleep(2)

white = driver.find_element_by_xpath("//span[text()='White']");
white.click()
time.sleep(2)

sparkling = driver.find_element_by_xpath("//span[text()='Sparkling']");
sparkling.click()
time.sleep(5)

driver.quit()
