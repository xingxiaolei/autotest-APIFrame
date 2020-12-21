#!/bin/bash
# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#--------------excel路径-------------

EXCEL_FILE_NAME = 'a.xlsx'
EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'data', EXCEL_FILE_NAME)

#--------------log日志路径------------
import datetime
LOG_FILE_NAME = '{}.log'.format(datetime.date.today())   # 以天来分割
# LOG_FILE_NAME = '{}.log'.format(datetime.date.strftime(datetime.date.today(), '%Y-%m'))   # 以月来分
LOG_FILE_PATH = os.path.join(BASE_DIR, 'log', LOG_FILE_NAME)


#---------------allure相关-------------
ALLURE_RESULTS = os.path.join(BASE_DIR, 'allure-results')
ALLURE_REPORT = os.path.join(BASE_DIR, 'allure-report')
ALLURE_COMMAND = 'allure generate {} -o {} --clean'.format(ALLURE_RESULTS, ALLURE_REPORT)


if __name__ == '__main__':
    s = {"userName": "admin", "password": "1234"}
    import jsonpath_rw
    r = jsonpath_rw.parse('userName').find(s)
    print(r)

