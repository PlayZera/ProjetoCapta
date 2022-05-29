import time
from main.Logger.Python.Logger import GerarLog
from selenium import webdriver

_log = GerarLog()

class TestarWebDeriver:

        def testar(self):
                _log.logger("Inicio de processo de captura de dados em página por documento.")
                driver = webdriver.Chrome('../WebDriver/chromedriver.exe')

                driver.get('http://www.google.com/')
                time.sleep(10)
                driver.quit()