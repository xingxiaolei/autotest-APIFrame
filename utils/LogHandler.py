#!/bin/bash
# -*- coding: utf-8 -*-

import os
import logging
from conf import settings

class LoggerHandler:

    #单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(LoggerHandler, cls).__new__(cls)
        return cls._instance

    def __init__(self, log_name, log_level, file_path, stream_level='info', file_level='warning'):
        self.logger_name = log_name
        self.logger_level = log_level
        self.file_path = file_path
        self.stream_level = stream_level
        self.file_level = file_level

        # 创建日志对象
        self.logger = logging.getLogger(self.logger_name)
        # 设置默认日志级别
        self.logger.setLevel(self.logger_level)
        # 设置日志输出流
        to_stream = logging.StreamHandler()
        to_file = logging.FileHandler(self.file_path)
        # 设置日志输出级别
        to_stream.setLevel(self.stream_level)
        to_file.setLevel(self.file_level)
        # 设置日志输出格式
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        to_stream.setFormatter(formatter)
        to_file.setFormatter(formatter)
        self.logger.addHandler(to_stream)
        self.logger.addHandler(to_file)



log = LoggerHandler(
    log_name='log',
    log_level=logging.INFO,
    file_path=settings.LOG_FILE_PATH,
    stream_level=logging.INFO,
    file_level=logging.INFO
)