from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")  #locator_amazon Logo
driver.find_element(By.id, "continue")   # locator_continue button
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")  # locator_need Help
driver.find_element(By.id, "createAccountSubmit") # create your amazon account
driver.find_element(By.XPATH, "//a[@class='a-link-normal']") # Create a free bussiness act
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")# Privacy notice
driver.find_element(By.XPATH, "//input[@type='email']")# Email field
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")# Conditions of use link
driver.find_element(By.XPATH, "//span[text()='Need help?' and @class='a-size-base a-link-normal']")# Need Help




