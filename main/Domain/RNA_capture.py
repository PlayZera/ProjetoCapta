import time

from selenium import webdriver

driver = webdriver.Chrome('../WebDriver/chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(10)

driver.quit()