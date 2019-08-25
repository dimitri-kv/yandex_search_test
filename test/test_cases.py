import pytest
import time
from utils.ImageCompare import two_images_difference
from test.SearchPage import SearchPage
from test.SearchResultPage import SearchResultPage
from test.TensorPage import TensorPage
from test.ImagesPage import ImagesPage
from selenium.webdriver.common.by import By

def test_search_page(driver, wait_for_element):
    d = driver
    d.get("https://yandex.ru")
    sp = SearchPage(d)
    sp.type_to_seach_field("Тензор")
    assert sp.get_suggestion() != []
    sp.run_search()
    srp = SearchResultPage(d)
    desired_block = -1
    link_count = 6
    for i in range(1, link_count):
        link = srp.site_link_text(i)
        if link == 'tensor.ru':
            desired_block = i
    if desired_block == -1:
        pytest.fail(f"link not found in {link_count} first blocks")
    tp = TensorPage(d)
    srp.click_on_result(desired_block)
    d.switch_to.window(d.window_handles[1])
    wait_for_element(d, 5, By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]")
    assert tp.get_page_link() == 'https://tensor.ru/'


def test_images_page(driver):
    d = driver
    # зайти на яндекс
    d.get("https://yandex.ru")
    sp = SearchPage(d)
    # ссылка Картинки присутствует
    assert sp.is_images_presented()
    # кликаем на ссылку
    sp.go_to_images()
    # проверяем что перешли на yandex.ru/images
    assert d.current_url == 'https://yandex.ru/images/'
    image_page = ImagesPage(driver)
    # открываем первую картинку
    image_page.open_first_image()
    # приверяем что картинка открылась
    src = image_page.get_image()
    print(src)
    image_page.download_image(src, 'image1')
    # нажимаем вперед и проверяем что картинка изменилась
    image_page.click_right_button()
    src = image_page.get_image()
    print(src)
    image_page.download_image(src, 'image2')
    dif = two_images_difference("image1.jpg", "image2.jpg")
    assert dif[0] == -1
    # нажимаем назад и проверяем что получили предыдущую картинку
    image_page.click_left_button()
    src = image_page.get_image()
    print(src)
    image_page.download_image(src, 'image3')
    dif = two_images_difference('image1.jpg', 'image3.jpg')
    assert dif[0] < 10.0
