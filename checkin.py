#!/usr/bin/env python3

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions




if len(sys.argv) != 1:
	print("""
	Does not require system arguments.
	Correct usage - checkin.py
	""")
	exit()

print("Ensure flightNumber.txt is updated with the flight number.")

options = FirefoxOptions()
#options.add_argument("--headless")
gd = os.path.abspath("./Dependencies\geckodriver")
driver = webdriver.Firefox(options=options, executable_path=gd, service_log_path=os.path.devnull)

flightNumber = open("./flightNumber.txt", "r").read()
print("Checking in with flight number:", flightNumber + ".")

def clickButton(selector, text):
        if selector == "xpath":
                driverWait(selector, text)
                driver.find_element_by_xpath("//button[contains(.,'" + text + "')]").click()
        elif selector == "class":
                driverWait(selector, text)
                driver.find_element_by_class_name(text).click()
        else:
                print("Unknown selector, returning.")   

def errorCheck(selector, error):
        if selector == "class":
                element = driver.find_elements_by_class_name(error)
                if len(element):
                        print(":( ", error, "found, exiting.")
                        time.sleep(2)
                        driver.quit()
                        exit()
                else:
                        print(":)  ", error, "not found, continuing.")
        elif selector == "id":
                element = driver.find_elements_by_id(error)
                if len(element):
                        print(":(  ", error, "found, exiting.")
                        time.sleep(2)
                        driver.quit()
                        exit()
                else:
                        print(":) ", error, "not found, continuing.")
        else:
                print("Unknown selector, returning.")

def driverWait(selector, text):
        if selector == "class":
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, text)))
        elif selector == "id":
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, text)))
        elif selector == "xpath":
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.xpath, "//button[contains(.,'" + text + "')]")))
        else:
           print("Unknown selector, returning.")     
                
        
def pageOne():
        print('Starting page 1.')
        
        #Open Starter page
        driver.get("https://www.qantas.com/au/en/travel-info/check-in.html")

        #Wait for page loaded
        driverWait("class", "qfa1-input")
        print("Page 1 loaded.")

        #Input from class and continue
        inputs = driver.find_elements_by_class_name('qfa1-input')
        inputs[0].send_keys(flightNumber)
        inputs[1].send_keys("Scroggie")
        clickButton("class", "qfa1-submit-button__button")

        #Error checks
        print("Checking for valid booking reference.")
        errorCheck("class", "form-validation-summary")

def pageTwo():
        print('Starting page 2.')
        
        #Wait for page loaded
        driverWait("id", "ts-status-message-default")
        print("Page 2 loaded.")
        
        #Error checks
        print("Checking if already checked in.")
        errorCheck("id", "un-checkin-button")
        print("Checking if too early to check in.")
        errorCheck("id", "ts-status-message-default")

        #Wait for button clickable and continue.
        clickButton("xpath", "Continue")

def pageThree():
	print('Starting page 3.')
	
	#Wait for button clickable and continue.
	clickButton("xpath", "Continue")
	print("Page 3 loaded.")

def pageFour():
	print('Starting page 4.')
	
        #Check page is clickable
	clickButton("id", "noBTN")
	print("Page 4 loaded.")
	
	#Wait for button clickable and continue.
	clickButton("xpath", "Check")

def main():
	pageOne()
	pageTwo()
	pageThree()
	pageFour()
	driver.quit()
	exit()

if __name__ == "__main__":
	main()
