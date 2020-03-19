class MainPage:
    def __init__(self,driver):
        self.driver = driver
        self.driver.get('https://www.amazon.com.br/')

    def search(self, key):
        search = self.driver.find_element_by_name('field-keywords')
        search.send_keys(key)

    def submit(self):
        btn = self.driver.find_element_by_css_selector('#nav-search > form > div.nav-right > div > input')
        btn.click()
        return self.driver.current_url