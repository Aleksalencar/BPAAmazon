'''
Script para listar o nome e o preço de produtos na Amazon
'''
from webdriver import Driver
from page_objects import MainPage
from page_objects import ListPage
from page_objects import ProductPage
from excel import ExcelManeger

d = Driver.Driver().driver
key = 'iphone'
mp = MainPage.MainPage(d)
mp.search(key)
ad = mp.submit()
lp = ListPage.ListPage(d, ad)
ids = lp.get_products_id()
products = []
ex = ExcelManeger.Excel(key)
for id in ids:
    product = []
    pp = ProductPage.ProductPage(d, id)
    product.append(pp.get_name())
    product.append(pp.get_price())
    ex.insert_row(product)



