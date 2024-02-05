from uuid import uuid4
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
mobile_emulation = { "deviceName": "iPhone XR" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument("--disable-extensions")
options.add_argument("--user-data-dir=/home/josgon/.config/google-chrome")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Number of times to repeat the search process
num_searches = 25

# Loop to repeat the search process
for i in range(num_searches):
    # Generate a random GUID
    search_query = str(uuid4().hex)[randint(0,18):randint(18,35)]
    print(len(search_query), search_query)

    # Navigate to Bing.com
    driver.get('http://www.bing.com')

    # Find the search input element by its name attribute
    search = driver.find_element(by=By.NAME, value="q")

    # Enter the search query    
    search.send_keys(search_query)
    
    # Submit the search form
    search.send_keys(Keys.RETURN)
    sleep(randint(5,8))

# Close the browser
driver.quit()