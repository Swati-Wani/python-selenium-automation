from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
#driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
#service = Service(driver_path) in newer version we dont need this
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
#click account button
driver.find_element(By.XPATH, "//span[text()='Account']").click()
sleep(5)

#verify text
expected_text= 'Sign in or create an account'
actual_text=driver.find_element(By.XPATH, "//div[@class='h-padding-b-tight']").text
assert expected_text in actual_text, f'Expected Text {expected_text} not in actual text {actual_text}'
sleep(5)
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")