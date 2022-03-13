import time

from selenium import webdriver


class Teste():

    def testeChrome():

        driver = webdriver.Chrome('../WebDriver/chromedriver.exe')

        driver.get('http://www.google.com/')

        time.sleep(10)

        driver.quit()
