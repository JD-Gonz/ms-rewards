from uuid import uuid4
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--user-data-dir=/home/josgon/.config/google-chrome")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

for i in range(randint(31,36)):
    # Navigate to Bing.com
    driver.get('http://www.bing.com')

    # Find the search input element by its name attribute
    search = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME,"q")))

    # Generate a random GUID
    search_query = str(uuid4().hex)[randint(1,18):randint(18,35)]
    print(i, len(search_query), search_query)

    # Enter the search query
    search.send_keys(search_query)
    sleep(1)

    # Submit the search form
    search.send_keys(Keys.RETURN)
    sleep(randint(5,8))

# Close the browser
driver.quit()