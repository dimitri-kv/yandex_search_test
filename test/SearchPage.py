from test.BasePom import BasePom
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class SearchPage(BasePom):
    def is_images_presented(self):
        try:
            self.driver.find_element(By.XPATH, "//a[contains(text(),'Картинки')]")
            return True
        except NoSuchElementException:
            print(f"link to Картинки not found")
            return False

    def go_to_images(self):
        elem = self.driver.find_element(By.XPATH, "//a[contains(text(),'Картинки')]")
        elem.click()

    def type_to_seach_field(self, query):
        self.driver.find_element(By.ID, 'text').send_keys(query)

    def run_search(self):
        self.driver.find_element(By.ID, "text").send_keys(Keys.ENTER)

    def get_suggestion(self):
        suggestions = self.driver.find_elements_by_class_name('suggest2-item__text')
        print(suggestions)
        for suggestion in suggestions:
            print(suggestion.text)
        return suggestions
