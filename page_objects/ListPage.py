from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ListPage:
    def __init__(self, driver,addres):
        self.driver = driver
        self.driver.get(addres)

    def get_products_id(self):
        wait = WebDriverWait(self.driver, 10)
        results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@data-cel-widget, 'search_result')]")))
        data_asin = []
        for element in results:
            data_asin.append(element.get_attribute("data-asin"))
        return data_asin