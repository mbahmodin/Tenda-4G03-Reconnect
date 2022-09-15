#!/usr/bin/python
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

parser = argparse.ArgumentParser(description='Reconnect Modem Tenda')
parser.add_argument('--ip',
                    action='store',
                    type=str,
                    default="192.168.11.1",
                    help='ip modem yang mau di reconnect')
args = parser.parse_args()

chrome_options = Options()
chrome_options.add_argument("--headless")

s = Service('/usr/bin/chromedriver')

driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get(f"http://{args.ip}/login.html")

exit = len(driver.find_elements(
    By.XPATH, "//a[contains(text(),\'Exit\')]"))
if driver.execute_script("return (arguments[0] == 0)", exit):
    driver.find_element(By.ID, "login-password").click()
    driver.find_element(By.ID, "login-password").send_keys("admin1")
    driver.find_element(By.ID, "subBtn").click()

WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(
    (By.CSS_SELECTOR, "#\\34GStatusNumber > .line-status-up")))
try:
    driver.find_element(
        By.CSS_SELECTOR, "#\\34GStatusNumber > .line-status-up").click()
except:
    driver.find_element(
        By.XPATH, "//*[@id=\"disConnectedWrap\"]/div[3]/div").click()

driver.switch_to.frame(0)
disconnected = len(driver.find_elements(
    By.XPATH, "//div[text()=\"Disconnected\"]"))

print(f"{args.ip} disconncted" if disconnected > 0 else f"{args.ip} conncted")

if driver.execute_script("return (arguments[0] > 0)", disconnected):
    driver.find_element(
        By.XPATH, "//input[@id=\"wan_submit\"][@value=\"Connect\"]").click()
driver.quit()
