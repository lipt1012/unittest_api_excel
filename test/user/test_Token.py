# coding:utf-8
from selenium import webdriver
import unittest
import time
import sys
sys.path.append("../..")  # 提升2级到项目根目录下
from config.config import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入
sys.path.append('..')
from config.config import *
sys.path.append('../')
from basecase import  BaseCase

class TestToken(BaseCase):    
    u'''颁发Token'''

    def test_CreateToken(self):
        u'''颁发token'''
        case_data = self.get_case_data("test_CreateToken")
        self.send_request(case_data)
if __name__ == "__main__":
    unittest.main(verbosity=2)
