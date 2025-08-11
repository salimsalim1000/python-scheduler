import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# ⛔ DO NOT hardcode sensitive info
email = os.getenv("TAGGED_EMAIL")
password = os.getenv("TAGGED_PASSWORD")

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920,1080') 
driver = webdriver.Chrome(options=chrome_options)

# Go to login page
driver.get("https://m.tagged.com/login/sign-in")
sleep(4)
driver.execute_cdp_cmd("Emulation.setPageScaleFactor", {"pageScaleFactor": 0.25})
# Login form
email_input = driver.find_element(By.NAME, 'username')
email_input.send_keys(email)

password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys(password)
driver.save_screenshot("beforelogin.png")
login_button = driver.find_element(By.CLASS_NAME, 'login')
login_button.click()

# Go to browse page
driver.get("https://m.tagged.com/browse")
sleep(10)
driver.save_screenshot("afterlogin.png")
driver.get("https://m.tagged.com/browse")
sleep(10)

driver.save_screenshot("screenshot.png")
# Repeat message logic
for _ in range(1):
    elements = driver.find_elements(By.CLASS_NAME, 'icon-message-on')
    filename = f"afterlogin_{_}.png"
    driver.save_screenshot(filename)
    if elements:
        for i in elements:
            sleep(2)
            try:
                i.click()
                sleep(2)

                # Wait for the message textarea to appear
                textarea = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div/div/form/div/textarea"))
                )
                textarea.send_keys("hi sexy .. did u have strapon")

                # Click send
                sendit = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div/div/form/button"))
                )
                sendit.click()
                sleep(1)
            except:
                pass

    # Go to next page
    try:
        nextpage = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[7]/div/div/div[1]/div[2]/div/a[7]"))
        )
        nextpage.click()
        sleep(20)
    except:
        print("No more pages or 'Next' button not found.")
        break
driver.save_screenshot("lastthing.png")
driver.quit()
