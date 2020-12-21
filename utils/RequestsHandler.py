#!/bin/bash
# -*- coding: utf-8 -*-

import requests
import re
import json
import jsonpath_rw
from utils.LogHandler import log


class RequestsOperate(object):

    def __init__(self, current_case, case_list=None):
        self.current_case = current_case
        self.case_list = case_list

    def get_response(self):
        response = requests.request(
            method=self.current_case['method'],
            url=self.current_case['url'],
            data=self._check_data(self.current_case['data']),
            params=self._check_params(self.current_case['params']),
            headers = self._check_headers(self.current_case['headers']),
            verify = False,
            timeout=120
        )
        self._write_data(response)
        return response.json(), json.loads(self.current_case['expect'])

    def _write_data(self, response):
        '''
        将当前强求的响应头和响应体 写入当前case中
        :param response:
        :return:
        '''
        for case in self.case_list:
            if case['case_num'] == self.current_case['case_num']:
                case['tmp_response_headers'] = response.headers
                case['tmp_request_headers'] = self.current_case['headers']
                case['tmp_request_params'] = self.current_case['params']
                case['tmp_request_data'] = self.current_case['data']

                case['tmp_response_headers'] = response.headers
                if 'application/json' in response.headers['Content-Type']:
                    case['tmp_response_json'] = response.json()
                if response.cookies.get_dict():
                    case['tmp_response_cookies'] = response.cookies.get_dict()
                else:
                    case['tmp_response_cookies'] = {}

    def _check_re(self, params):
        '''检查data 和 param中是否有要替换的参数
        {"testfan-token": "${neeo_001>response_json>data}$", "userName": "${neeo_001>request_headers>userName}$"}
        '''
        pattern = re.compile('\${(.*?)}\$')
        match_list = pattern.findall(params) #匹配所有，结果为列表
        if match_list:
            for match in match_list:
                case_num, params_type, path = match.split('>')
                for case in self.case_list:
                    if case_num == case['case_num']:
                        tmp_data = case['tmp_{}'.format(params_type)]
                        tmp_data = json.loads(tmp_data)

                        rule_data = jsonpath_rw.parse(path).find(tmp_data)
                        if rule_data:
                            rule_data = [i.value for i in rule_data][0]
                            params = re.sub(pattern=pattern, repl=rule_data, string=params, count=1)
                        else:
                            log.logger.error('{}参数替换错误'.format(case_num))
            return json.loads(params)

        else: #如果没有要替换的参数，转化成字典直接返回
            return json.loads(params)

    def _check_data(self, data):
        '''处理data参数'''
        if data:
            data = self._check_re(data)
            return data
        else:
            return {}

    def _check_params(self, params):
        '''处理params参数'''
        if params:
            params = self._check_re(params)
            return params
        else:
            return {}

    def _check_headers(self, headers):
        '''处理headers'''
        if headers:
            headers = self._check_re(headers)
            return headers
        else:
            return {}