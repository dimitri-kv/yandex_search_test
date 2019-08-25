import requests
from test.BasePom import BasePom
from selenium.webdriver.common.by import By

class ImagesPage(BasePom):
    def run_search(self, query):
        pass

    def is_images_presented(self):
        pass

    def go_to_images(self):
        pass

    def open_first_image(self):
        elem = self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        elem.click()

    def click_right_button(self):
        elem = self.driver.find_element(By.XPATH,
                                        "//div[@title='Следующая']//a[contains(@class,'cl-layout__nav__arrow')]")
        elem.click()

    def click_left_button(self):
        elem = self.driver.find_element(By.XPATH,
                                        "//div[@title='Предыдущая']//a[@class='cl-layout__nav__arrow']")
        elem.click()

    def get_image(self):
        elem = self.driver.find_element(By.XPATH, "//img[@class='image__image']")
        if 'ng-hide' in elem.get_attribute('class'):
            print('Image is not visible on screen')
            return 'Image is hidden'
        return elem.get_attribute('src')

    def download_image(self, src, image_name):
        with open(f'{image_name}.jpg', 'wb') as handle:
            response = requests.get(src, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
        return response


