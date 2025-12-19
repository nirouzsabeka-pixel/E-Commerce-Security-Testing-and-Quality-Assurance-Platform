from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

service = Service(r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://demowebshop.tricentis.com")
time.sleep(5)
driver.quit()
