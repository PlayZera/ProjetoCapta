from email.headerregistry import ContentTransferEncodingHeader
import time
from main.Logger.Python.Logger import GerarLog

from selenium import webdriver

_log = GerarLog()

class Capture():
    
    def captureFromFile():

        _log.logger("Inicio de processo de captura de dados em página por documento.")

        driver = webdriver.Chrome('../WebDriver/chromedriver.exe')

        driver.get('http://www.google.com/')

        time.sleep(10)

        driver.quit()
