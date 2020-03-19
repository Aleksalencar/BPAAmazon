class ProductPage:
    def __init__(self, driver, id):
        addres = "https://www.amazon.com.br/dp/" + id
        self.driver = driver
        self.driver.get(addres)

    def get_name(self):
        name = "Not available"
        try:
            name = self.driver.find_element_by_xpath("//*[@id = 'ebooksProductTitle'] | //*[@id = 'productTitle']")
            name = name.text
        except:
            pass

        return name

    def get_price(self):
        price = "Not available"
        try:
            price = self.driver.find_element_by_xpath(
                "//*[@id = 'priceblock_ourprice'] | //*[@class = 'a-size-medium a-color-price']")
            price = price.text
        except:
            pass
        return price
