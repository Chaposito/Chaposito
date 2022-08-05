import search
import common
import image
from loguru import logger

logger.add("log.txt", format = "{time} {level} {message}",
            level = "INFO", rotation = "100 KB", compression = "zip")

@logger.catch
def test_task_tensor():
    common.open("https://yandex.ru/")
    search.input_search("Тензор")
    search.check_suggest()
    search.click_search()
    common.check_go_to_page("search")
    search.check_search_tensor("https://tensor.ru/")
    common.quit()
    
@logger.catch
def test_task_image():
    common.open("https://yandex.ru/")
    search.click_on("Картинки")
    common.change_tab(1)
    common.check_go_to_page("images")
    image.click_on_popular_request()
    img1 = image.click_on_image()
    img2 = image.next_image()
    image.compare_images_not_equals(img1, img2)
    img3 = image.back_image()
    image.compare_images_equals(img1, img3)
    common.quit()
