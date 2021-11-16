import time
import os
import argparse


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pyvirtualdisplay import Display 

def getDriver(showDisplay):

    '''
    Main logic behind creating a driver object to use FireFox web browser
    Arguments:
        url(str): Target url
    
    Returns:
        Firefox webdriver instance in python
    '''
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True
    firefox_options = webdriver.FirefoxOptions()
    if (showDisplay != 1):
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--disable-gpu")
    driver = webdriver.Firefox(firefox_options = firefox_options,firefox_profile = profile)
    # driver.get(url)
    return driver

username = "test-1"
oldPassword = "Oldpassword@1"
name = "Test 1"
email = "test1@test.com"
newPassword = "NewPassword@1"



if __name__== "__main__":
    parser = argparse.ArgumentParser(description = \
        "Arguments for program")

    parser.add_argument('-url', type=str, \
                    help='Target Website URL', default = 'http://127.0.0.1:8080/')
    parser.add_argument('-d', metavar = 'display', type=int, \
        help='Time to sleep between crawling of website links', default = 0)
    
    args = parser.parse_args()

    showDisplay = args.d
    url = args.url
    print(showDisplay)

    if (showDisplay != 1):

        DISPLAY_VISIBLE = 0
        DISPLAY_WIDTH = 2400
        DISPLAY_HEIGHT = 1000
        # print(os.environ['DISPLAY'])
        # start display 
        display = Display(visible=DISPLAY_VISIBLE, size=(DISPLAY_WIDTH, DISPLAY_HEIGHT), backend="xvfb", use_xauth=True)
        display.start()
        print(os.environ['DISPLAY'])

    print("Starting up bot")  
    driver = getDriver(showDisplay)

    from Actions import (register, resting_mouse, changePassword, logout, login)


    driver.get(url)

    #maximise browser window
    driver.maximize_window()
    # driver.set_window_size(2300, 900)

    print("start register")
    register(driver, username, oldPassword, name, email)
    print("end register")

    print("start change password")
    changePassword(driver, oldPassword, newPassword)
    print("end change password")

    print("start logout")
    logout(driver)
    print("end logout")

    print("start logout")
    login(driver, username, newPassword)
    print("end logout")

    driver.quit()

    if (showDisplay != 1):
        display.stop()

    print("Shutting down bot")