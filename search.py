from uuid import uuid4
from time import sleep
from random import randint
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def bingSearch(driver, num, sleepInterval):
    occurances = num + randint(1, 5)
    for i in range(occurances):
        # Navigate to Bing.com
        driver.get('http://www.bing.com')

        if i == 0:
            sleep(5)
        elif i % 4 == 0 and i <= num:
            print(datetime.now().strftime("%H:%M:%S") + f": Going to sleep for {sleepInterval} min")
            sleep(sleepInterval * 60)
            driver.get('http://www.bing.com')
            sleep(2)

        # Find the search input element by its name attribute
        search = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME,"q")))

        # Generate a random GUID
        search_query = str(uuid4().hex)[randint(1,18):randint(18,35)]
        print(i + 1, len(search_query), search_query)

        # Enter the search query
        search.send_keys(search_query)
        sleep(1)

        # Submit the search form
        search.send_keys(Keys.RETURN)
        sleep(randint(5,8))

    # Close the browser
    driver.quit()
