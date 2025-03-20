import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException

# Initialize ChromeDriver
driver = webdriver.Chrome()

# Navigate to a website
driver.get('https://teledeclaration.cnas.dz')

# Do your tasks...
time.sleep(6)
def wait_for_element_not_display_block(driver, element_id, timeout=20, retry_interval=0.5, max_retries=3):
    attempts = 0
    while attempts < max_retries:
        try:
            WebDriverWait(driver, timeout).until(
            lambda d: 'display: block' not in d.find_element(By.ID, element_id).get_attribute('style'))
            return True
        except StaleElementReferenceException:
            time.sleep(retry_interval)
            attempts += 1
    raise Exception("Exceeded maximum retries for ensuring element is not display: block")

# Find the element by class name and click it
try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="myModal"]/div[2]/div/div/div/div[2]/div/div/div[3]/a[2]'))
    )
    element.click()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/section[1]/div/div[1]/div/div[1]/form/div[1]/div[1]/div/input'))
    )
    username_input.send_keys('39120000')  # Replace with actual username
except Exception as e:
    print(f"An error occurred while entering username: {e}")

try:
    pass_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/section[1]/div/div[1]/div/div[1]/form/div[1]/div[2]/div/input'))
    )
    pass_input.send_keys('00000000')  # Replace with actual username
except Exception as e:
    print(f"An error occurred while entering username: {e}")

# Optionally, submit the form or click the login button
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/section[1]/div/div[1]/div/div[1]/form/div[3]/div/div[1]/div[1]/input'))  # Replace with actual login button XPath
    )
    login_button.click()
except Exception as e:
    print(f"An error occurred while clicking the login button: {e}")

try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="myModal"]/div/div/div/div/div[2]/div/div/button'))
    )
    button.click()
except Exception as e:
    print(f"An error occurred while clicking the button: {e}")

try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div[2]/div/div[2]/div/div/div[2]/div[5]'))
    )
    button.click()
except Exception as e:
    print(f"An error occurred while clicking the button: {e}")

try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div/div[1]/form/div[10]/div[1]/div/div/div[1]/div[1]/div/div[2]'))
    )
    '''button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="finit:j_idt44:1"]'))
    )'''
    button.click()
except Exception as e:
    print(f"An error Affiliation button: {e}")


def retry_on_stale_reference(driver, locator, timeout=10, retry_interval=0.5, max_retries=3):
    attempts = 0
    while attempts < max_retries:
        try:
            element = WebDriverWait(driver, timeout).until( EC.presence_of_element_located(locator) )
            return element
        except StaleElementReferenceException:
            time.sleep(retry_interval)
            attempts += 1
    raise Exception("Exceeded maximum retries for locating element without stale reference")

file_path = 'cnas.xlsx'
df = pd.read_excel(file_path)
print(df)
for index, num in df.iterrows():
    if not pd.isna(num['NUMSS']) and len(str(num['NUMSS'])) >= 12:  # Make sure 'NUMSS' is a column in your DataFrame
        print(f"Row {index}: NUMSS is {num['NUMSS']}")

        try:
            # Wait for the input field to be visible
            codecnas_input = retry_on_stale_reference(driver, (By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div/div[1]/form/div[10]/div[1]/div/div/div[1]/div[2]/input'))
            codecnas_input.click()  # Click to focus on the input
            codecnas_input.send_keys(Keys.CONTROL, 'a')  # Select all text (use 'a' for Mac)
            codecnas_input.send_keys(Keys.DELETE)  # Delete the selected text

            # Now you can send new keys to the input field
            codecnas_input.send_keys(num['NUMSS'])  # Replace with actual value
            input_valuecode = codecnas_input.get_attribute('value')
            df.at[index, 'newnb'] = input_valuecode
            # Wait for the AJAX request to complete and the overlay to be hidden

            # Wait for a moment to ensure the value is set
            #time.sleep(2)

            # Handle the next textbox
            try:
                textboxforevent = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                '/html/body/div[2]/div[2]/div/div[2]/div/div/div[1]/form/div[10]/div[1]/div/div/div[3]/div[2]/div[1]/div/div[2]/div[1]/input'))
                )
                textboxforevent.click()
                print('before')

                WebDriverWait(driver, 20).until(
                    lambda d: 'display: block' not in d.find_element(By.ID, 'finit:j_idt48_blocker').get_attribute(
                        'style'))  # Ensure the overlay for the next textbox is also hidden
                print('After the one')
                WebDriverWait(driver, 20).until( lambda d: 'display: block' not in d.find_element(By.ID, 'finit:j_idt48_blocker').get_attribute('style') )
                print('After')
                #time.sleep(2)
            except Exception as e:
                print(f"An error occurred while clicking the text box for events: {e}")

        except Exception as e:
            print(f"An error occurred in the code for CNAS: {e}")


        try:
            # Retry locating the elements in case of stale reference
            name_element = retry_on_stale_reference(driver, (By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div/div[1]/form/div[10]/div[1]/div/div/div[3]/div[2]/div[1]/div/div[2]/div[1]/input'))
            name_value = name_element.get_attribute('value')
            df.at[index, 'newNOMA'] = name_value
            newPRENOMA_element = retry_on_stale_reference(driver, (By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div/div[1]/form/div[10]/div[1]/div/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/input'))
            newPRENOMA_value = newPRENOMA_element.get_attribute('value')
            df.at[index, 'newPRENOMA'] = newPRENOMA_value
            newNOMARAB_element = retry_on_stale_reference(driver, (By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div/div[1]/form/div[10]/div[1]/div/div/div[3]/div[2]/div[1]/div/div[2]/div[2]/input'))
            newNOMARAB_value = newNOMARAB_element.get_attribute('value')
            df.at[index, 'newNOMAR'] = newNOMARAB_value
            newPRENOMAAR_element = retry_on_stale_reference(driver, (By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div/div[1]/form/div[10]/div[1]/div/div/div[3]/div[2]/div[2]/div/div[2]/div[2]/input'))
            newPRENOMAAR_value = newPRENOMAAR_element.get_attribute('value')
            df.at[index, 'newPRENOMAAR'] = newPRENOMAAR_value
            newDATNAIS_element = retry_on_stale_reference(driver, (By.XPATH, '//*[@id="finit:date_input"]'))
            newDATNAIS_value = newDATNAIS_element.get_attribute('value')
            df.at[index, 'newDATNAIS'] = newDATNAIS_value
            print(newDATNAIS_value)
            print(name_value)


        except:
            pass
        df.at[index, 'state'] = 'UPDATED'



    # Display the DataFrame



df.to_excel('cnas web site.xlsx', index=False)

print("Values updated and saved to 'cnas web site.xlsx'")
time.sleep(30000)
driver.quit()
