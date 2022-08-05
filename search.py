from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import common
from loguru import logger


def input_search(text):
    global search
    try:
        search = common.browser.find_element(By.ID, "text")
    except:
        common.quit()
        raise NoSuchElementException("Не найдено поле поиска")
    search.send_keys(text)
    logger.info("Text entered in the search field: " + text)
    
def click_on(link):
    try:
        icon = common.browser.find_element(By.LINK_TEXT, link)
    except NoSuchElementException:
        common.quit()
        raise NoSuchElementException("Не найдена иконка " + link)
    icon.click()
    logger.info("Moved to the page: " + link)
     
def check_suggest():
    try:
        lst = common.browser.find_element(By.CLASS_NAME, "mini-suggest__popup-content")
    except NoSuchElementException:
        common.quit()
        raise NoSuchElementException("Не найдена таблица с подсказками")
    logger.info("Confirming the presence of a field with hints")
        
def click_search():
    but = common.browser.find_element(By.CLASS_NAME, "mini-suggest__button")
    but.click()
    logger.info("Searched")

def check_search_tensor(url):
    result = common.browser.find_element(By.CLASS_NAME, "Link_theme_outer").get_attribute("href")
    assert result == url, "Сайт " + url + " не является первым в поисковой выдаче"
    logger.info("Checked for the presence of an address: " + url + ". in the first position of the search")
