import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import itertools
from base64 import b64decode,b64encode
import os
import threading
import sys

warnings.filterwarnings("ignore")
subscribers = 0

print("""
$$$$$$$$\  $$$$$$\     $$$$$$$$\                                          
$$  _____|$$  __$$\    \__$$  __|                                         
$$ |      $$ /  \__|      $$ | $$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$$\ 
$$$$$\    $$ |$$$$\       $$ |$$  __$$\  \____$$\ $$  _$$  _$$\ $$  _____|
$$  __|   $$ |\_$$ |      $$ |$$$$$$$$ | $$$$$$$ |$$ / $$ / $$ |\$$$$$$\  
$$ |      $$ |  $$ |      $$ |$$   ____|$$  __$$ |$$ | $$ | $$ | \____$$\ 
$$ |      \$$$$$$  |      $$ |\$$$$$$$\ \$$$$$$$ |$$ | $$ | $$ |$$$$$$$  |
\__|       \______/$$$$$$\\__| \_______| \_______|\__| \__| \__|\_______/ 
                   \______|                                               
""")

print("Please donate on paypal for more softwares like this paypal : mohammedmusthafa9512@gmail.com")

id = "" #your channel id here
password = ''# your password here

Done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if Done:
            break
        sys.stdout.write("\rHacking google server-------"+c)
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\nDone! successfully hacked")

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
Done = True

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options)


def Stuff(driver):
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(22)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def subscribe():
    driver.find_element(By.XPATH, "//*[@class='btn-step']").click()


def confirm():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Confirm"))).click()


driver.get("https://www.subpals.com/login/final/" + str(id) + "/")

enter = driver.find_element_by_xpath(
    "/html/body/div[1]/section/div/div/div/div/div/form/div[2]/input"
)
enter.send_keys(password)

driver.find_element(By.XPATH, "//button[@class='btn btn-login']").click()

try:
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/a"))
            ).click()
except:
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "//a[@id='Cancel Activation']"))
        ).click()
    time.sleep(5)
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/section/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/a"))
            ).click()

time.sleep(4)

while True:
    subscribe()

    Stuff(driver)

    time.sleep(6)

    confirm()

    time.sleep(30)
    subscribers += 1

    print("increased", subscribers, "subs ✌😘😎😈")

    if subscribers == 6:
        time.sleep(10)
        driver.quit()
        break


print("you will get 6 subscribers")
