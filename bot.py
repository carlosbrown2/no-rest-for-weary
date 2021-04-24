from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
# Initiate the browser
options = Options()
options.headless = True 
browser  = webdriver.Chrome(ChromeDriverManager().install(), options=options)

browser.get('https://divscreener.herokuapp.com/')
sleep(3)
browser.quit()

