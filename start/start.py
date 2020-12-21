#!/bin/bash
# -*- coding: utf-8 -*-

import os
from conf import settings
import subprocess

if __name__ == '__main__':
    import pytest
    os.chdir(settings.BASE_DIR)  # 切换工作目录，使pytest能找到pytest.ini文件，进而根据配置文件执行测试用例

    pytest.main()

    subprocess.call(settings.ALLURE_COMMAND, shell=False)
    # os.system(settings.ALLURE_COMMAND)