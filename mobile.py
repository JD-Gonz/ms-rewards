from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from search import bingSearch

options = Options()
mobile_emulation = { "deviceName": "iPhone XR" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument("--disable-extensions")
options.add_argument("--user-data-dir=/home/josgon/.config/google-chrome")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

bingSearch(driver, randint(20,24))

