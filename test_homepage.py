from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("./drivers/chromedriver.exe")
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.zee5.com")
    wait = WebDriverWait(driver, 15)

    
    try:
        cookie_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        cookie_btn.click()
        print(" Cookie popup closed.")
    except:
        print(" No cookie popup found, continuing...")

    buy_plan = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Buy Plan']"))
    )
    buy_plan.click()
    print(" 'Buy Plan' button clicked successfully!")

    time.sleep(3)
    driver.save_screenshot("after_click.png")
    print(" Screenshot saved as 'after_click.png'")

except Exception as e:
    print(" Test failed:", e)
    driver.save_screenshot("error_screenshot.png")

finally:
    driver.quit()
