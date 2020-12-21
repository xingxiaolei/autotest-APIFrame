#!/bin/bash
# -*- coding: utf-8 -*-

import pytest
from deepdiff import DeepDiff
from utils.ExcelHandler import ExcelOpeate
from conf import settings
from utils.LogHandler import log
from utils.RequestsHandler import RequestsOperate

case_list = ExcelOpeate(settings.EXCEL_FILE_PATH, 3).get_data()

@pytest.mark.parametrize('item', case_list)
def test_case(item):
    result, expected = RequestsOperate(current_case=item, case_list=case_list).get_response()
    assert not DeepDiff(result, expected).get('values_changed', {})