from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
from selenium.webdriver import ActionChains
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image
import time
import easyocr
import os
import pdfkit
import codecs
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


while True:
    try:
        url = 'chrome://downloads/'
        driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        action_chains = ActionChains(driver)
        driver.get(url)
        driver.maximize_window()
        break
    except:
        print('selenium error occurred in downloading')
        driver.quit()