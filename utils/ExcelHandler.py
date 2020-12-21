#!/bin/bash
# -*- coding: utf-8 -*-

import xlrd

class ExcelOpeate(object):

    def __init__(self, file_path, sheet_by_index=0):
        self.file_path = file_path
        self.sheet_by_index = sheet_by_index

    def get_data(self):
        book = xlrd.open_workbook(self.file_path)
        sheet = book.sheet_by_index(self.sheet_by_index)

        title = sheet.row_values(0)

        return [dict(zip(title, sheet.row_values(line))) for line in range(1, sheet.nrows)]

if __name__ == '__main__':
    from conf import settings
    print(ExcelOpeate(settings.EXCEL_FILE_PATH, 0).get_data())