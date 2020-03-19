import os
from selenium import webdriver

class Driver:
    def __init__(self):
        root = os.path.dirname(os.path.abspath(__file__))
        path = root + "\\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=path)
