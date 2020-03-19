from openpyxl import Workbook
import os
import datetime


class Excel:
    def __init__(self, name):
        name = name+'_'
        self.wb = Workbook()
        root = os.path.dirname(os.path.abspath(__file__))
        currentDT = datetime.datetime.now()
        date = currentDT.strftime("%Y-%m-%d_%H_%M_%S")
        print(date)
        self.filepath = root + "\\" + name + date + ".xlsx"
        print(self.filepath)

    def insert_row(self, row):
        sheet = self.wb.active
        print(row)
        sheet.append(row)
        self.save()

    def save(self):
        self.wb.save(self.filepath)