from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import undetected_chromedriver as uc

import json

#Overloading how uc deletes once everything is done, I want to keep the window open
class ucOpen(uc.Chrome):
    def __del__(self):
        pass

def login_indeed(driver) -> bool:

    with open(r"C:\Users\parkf\Desktop\personalProjects\PythonWebCrawling\loginInfo.Json") as f:
        raw = json.load(f)
        email = raw["id"]
        pass_word = raw["password"]

    main_page = driver.current_window_handle
    driver.find_element(by=By.XPATH, value='//*[@id ="login-google-button"]').click()

    for handle in driver.window_handles:
        if handle is not main_page:
            login_page = handle

    driver.switch_to.window(login_page)

    driver.find_element(By.ID, value="identifierId").send_keys(email)
    driver.find_element(By.ID, value="identifierNext").click()
    driver.find_element(By.NAME, value="password").send_keys(pass_word)
    driver.find_element(By.ID, value="passwordNext").click()

    driver.implicitly_wait(20) #Check that we dual authenticated and keep 'er moving
    try:
        driver.find_element(By.ID, value="text-input-what")
    except:
        return False
    driver.implicitly_wait(5)
    return True

def main():
    driver = ucOpen(use_subprocess=True)
    driver.implicitly_wait(5)
    driver.get("https://secure.indeed.com/auth?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fwww.indeed.com%2F&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess&_ga=2.235105921.1025626514.1652310047-664962784.1652310047")

    if not login_indeed(driver): 
        print("Couldn't login")
        return

if __name__ == "__main__":
    main()
