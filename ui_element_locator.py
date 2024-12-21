from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys

def locate_ui_element(url, selector_type, selector_value):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disabel-gpu')
    service = Service('chromedriver')
    
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print(f"Accessing URL: {url}")
        driver.get(url)
        
        print(f"Locating element by {selector_type} with value {selector_value}")
    