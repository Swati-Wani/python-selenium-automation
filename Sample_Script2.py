from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
#search_box=driver.find_element(By.ID, "APjFqb")
search_box = driver.find_element(By.CSS_SELECTOR, '#APjFqb')
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.ENTER)
