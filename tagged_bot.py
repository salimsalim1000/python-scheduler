from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)

# Navigate to a webpage (replace with your target URL)
driver.get("https://m.tagged.com/login/sign-in")

sleep(4)
email_input = driver.find_element(By.NAME, 'username')
email_input.send_keys("salimsalim1000@yahoo.com")

# Find the password input field and enter your password
password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys("18071989")

# Find the login button and click it
login_button = driver.find_element(By.CLASS_NAME, 'login')
login_button.click()
driver.get("https://m.tagged.com/browse")

driver.get("https://m.tagged.com/browse")

sleep(3)
# Find all elements with the class name 'icon-on'
for tt in range(4):
    elements = driver.find_elements(By.CLASS_NAME, 'icon-message-on')

    #  driver.find_elements(By.CSS_SELECTOR, '.icon-message-on, .icon-on')
    # Click on the first matching element (if any)
    if elements:
        for i in elements:

            sleep(2)
            try:
                i.click()
                sleep(2)
                # Find the textarea for composing a message and send a message
                textareas = driver.find_element(By.CSS_SELECTOR, '.composer-input, .ng-pristine ,.ng-valid')
                sleep(2)
                textarea = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div/div/form/div/textarea"))
                )
                # textarea.send_keys("hola ... ¿Eres sumiso o dominante?")
                #textarea.send_keys("hi ... are u dominant lady or submassive?")
                textarea.send_keys("hi sexy .. did u have strapon ")
            #            textarea.send_keys("hola amor ... come esta")
                # Close the message window
                sendit = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div/div/form/button"))
                )
                sendit.click()
                sleep(1)
            except:
                pass
    nextpage = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div[7]/div/div/div[1]/div[2]/div/a[7]"))
    )
    nextpage.click()
    sleep(20)
driver.quit()
