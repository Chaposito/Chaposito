from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from loguru import logger
    
def open(url):
    global browser
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get(url)
    logger.info("The \"open\" function completed successfully. Execution artifacts: " + url)
    time.sleep(1) 
    
def check_go_to_page(page):
    time.sleep(1)
    url = browser.current_url
    spl = url.split("/")
    assert spl[3] == page, "Переход на страницу" + page + " не выполнен"
    logger.info("The \"check_go_to_page\" function completed successfully. Execution artifacts: " + page)
    
def quit():
    browser.quit()
    logger.info("Window closed successfully")
    
def change_tab(tab):
    new_window = browser.window_handles[tab]
    browser.switch_to.window(new_window)
    logger.info("Moved to tab " + str(tab + 1))