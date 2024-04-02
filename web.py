import sys
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from search import bingSearch

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--user-data-dir=/home/josgon/.config/google-chrome")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

bingSearch(driver, randint(30,32), int(sys.argv[1]))