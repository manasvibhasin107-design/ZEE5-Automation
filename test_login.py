from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://www.zee5.com")
    print(f"Page title: {driver.title}")

    try:
        cookie_close = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//button[contains(text(),'Accept') or contains(text(),'OK') or contains(@id,'onetrust-accept')]"
        )))
        cookie_close.click()
        print(" Cookie popup closed.")
        time.sleep(2)
    except Exception:
        print(" No cookie popup found or already closed.")

    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        print(" Header loaded.")
    except Exception:
        print(" Header not found — page may not have loaded correctly.")

    try:
        login_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//*[self::a or self::button or self::span][contains(text(),'Login') or contains(text(),'Sign In')]"
        )))
        driver.save_screenshot("before_login_click.png")
        print(" Screenshot before clicking Login saved.")

        driver.execute_script("arguments[0].click();", login_btn)
        print(" Login button clicked successfully (via JS).")

        time.sleep(3)
        driver.save_screenshot("after_login_click.png")
        print(" Screenshot after clicking Login saved.")
    except Exception as e:
        print(" Test failed:", e)
        driver.save_screenshot("error_login.png")

finally:
    driver.quit()
    print(" Browser closed.")
