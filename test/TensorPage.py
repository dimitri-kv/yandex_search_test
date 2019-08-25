from test.BasePom import BasePom

class TensorPage(BasePom):
    def get_page_link(self):
        return self.driver.current_url
