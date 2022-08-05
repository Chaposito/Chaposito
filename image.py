from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import common
from loguru import logger

def click_on_popular_request():
    pdp = common.browser.find_element(By.CLASS_NAME, "PopularRequestList-SearchText").text
    first = common.browser.find_element(By.CLASS_NAME, "PopularRequestList-Item_pos_0")
    first.click()
    inp = common.browser.find_element(By.CLASS_NAME, "input__control").get_property("value")
    assert inp == pdp, "Результаты поиска не совпадают"
    logger.info("Navigated to the popular query page. The query matches the name of the category.")
    
def click_on_image():
    img = common.browser.find_element(By.CLASS_NAME, "serp-item__link")
    img.click()
    try:
        check = common.browser.find_element(By.CLASS_NAME, "MMImageContainer")
    except NoSuchElementException:
        common.quit()
        raise NoSuchElementException("Картинка не открылась")
    time.sleep(1)
    img1 = common.browser.current_url
    logger.info("The image is opened. Url: " + img1)
    return img1
    
def next_image():
    next_img = common.browser.find_element(By.CLASS_NAME, "CircleButton_type_next")
    next_img.click()
    time.sleep(1)
    img2 = common.browser.current_url
    logger.info("Moved to next image. Url: " + img2)
    return img2

def compare_images_not_equals(img1, img2):
    assert img1 != img2, "Картинки совпадают"
    logger.info("Checked that the images are different")
    
def back_image():
    try:
        back = common.browser.find_element(By.CLASS_NAME, "CircleButton_type_prev")
    except NoSuchElementException:
        common.quit()
        raise NoSuchElementException("Картинка не открылась")
    back.click()
    time.sleep(1)
    img3 = common.browser.current_url
    logger.info("Move back an image. Url: " + img3)
    return img3
    
def compare_images_equals(img1, img2):
    assert img1 == img2, "Картинки не совпадают"
    logger.info("Checked that image 1 and 3 are the same")