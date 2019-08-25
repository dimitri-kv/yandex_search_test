from test.BasePom import BasePom
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SearchResultPage(BasePom):
    def site_link_text(self, block_number):
        elem = self.driver.find_element(By.XPATH,
                                        f"/html[1]/body[1]/div[3]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[{block_number}]")
        try:
            link_text = elem.find_element(By.XPATH, f".//div[1]/div[1]/div[1]/a[1]/b[1]")
        except NoSuchElementException:
            print(f"for block №{block_number} link not found")
            return None
        print(link_text.text)
        return link_text.text

    def click_on_result(self, block_number):
        elem = self.driver.find_element(By.XPATH,
        f"/html[1]/body[1]/div[3]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[{block_number}]/div[1]/div[1]/div[1]/a[1]/b[1]")
        elem.click()
        print("elem clicked")
