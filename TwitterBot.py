import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


profile_path = "C:/Users/timiv/AppData/Roaming/Mozilla/Firefox/Profiles/bb6892d4.default"


options = Options()


service = Service("C:/Users/timiv/Downloads/geckodriver-v0.35.0-win64/geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)
 
post = input("What would you like your post to say: ")
username = input("Enter username: ")
password = input("Enter password: ")

driver.get("https://x.com/")

signInBtn = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div").click()
time.sleep(1)
usernameTxtF = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input").send_keys(password)

nextBtn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div").click()
time.sleep(1)
passwrdTxtF = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(username)

delay=10
logIn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div"))).click()

postBtn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div"))).click()

test = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div"))).send_keys(post)















