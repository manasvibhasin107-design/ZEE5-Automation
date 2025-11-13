from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://www.zee5.com")
    print("Page title:", driver.title)
    time.sleep(5)

    try:
        cookie_close = driver.find_element(By.ID, "onetrust-close-btn-container")
        cookie_close.click()
        print(" Cookie popup closed.")
        time.sleep(2)
    except Exception:
        print(" No cookie popup found.")

    try:
        search_box = driver.find_element(By.ID, "searchInput")
        search_box.clear()
        search_box.send_keys("Family Man")
        search_box.send_keys(Keys.ENTER)
        print(" Search query entered.")
        time.sleep(5)
    except Exception as e:
        print(" Search box not found:", e)
        driver.save_screenshot("search_box_error.png")
        driver.quit()
        exit()

    page_source = driver.page_source
    if "Family" in page_source or "Man" in page_source:
        print(" Search results loaded successfully!")
    else:
        print(" No search results found.")

    driver.save_screenshot("search_results.png")
    print(" Screenshot saved as 'search_results.png'")

finally:
    driver.quit()
    print(" Browser closed.")
