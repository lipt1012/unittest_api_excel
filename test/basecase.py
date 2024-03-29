import unittest
import requests
import json
import sys
sys.path.append("../") 
from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入
from lib.get_token import getToken



class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(data_file, cls.__name__)

    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)

    def send_request(self, case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        #headers = case_data.get('headers')
        args = case_data.get('args')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')
        token = (getToken())
        headers = {"Content-Type":"application/json","Authorization":token}


        if method.upper() == 'GET':
            res = requests.get(url = url,data = json.loads(args),headers = json.loads(headers))
            log_case_info(case_name, url, args, expect_res, res.text)
            self.assertEqual(res.status_code,200)
            #self.assertEqual(res.text, expect_res)

        elif method.upper() == 'POST':
            res = requests.post(url = url,data = args,headers = headers)
            log_case_info(case_name, url, args, expect_res, res.text)
            self.assertEqual(res.status_code,200)
            #self.assertEqual(res.text, expect_res)
            

            

        elif method.upper() == 'PUT':
            res = requests.put(url = url,data = json.loads(args),headers = json.loads(headers))
            log_case_info(case_name, url, args, expect_res, res.text)
            self.assertEqual(res.status_code,200)
            self.assertEqual(res.text, expect_res)

        else :
            res = requests.delete(url = url,data = json.loads(args),headers = json.loads(headers))
            log_case_info(case_name, url, args, expect_res, res.text)
            self.assertEqual(res.status_code,200)
            self.assertEqual(res.text, expect_res)

        # elif data_type.upper() == 'FORM':
        #     res = requests.post(url=url,data=json.loads(args))
        #     log_case_info(case_name, url, args, expect_res, res.text)
        #     self.assertEqual(res.text, expect_res)

        # else:
        #     res = requests.post(url=url, json=json.loads(args))
        #     log_case_info(case_name, url, args, json.dumps(json.loads(expect_res), sort_keys=True),
        #                   json.dumps(res.json(), ensure_ascii=False, sort_keys=True))
        #     self.assertDictEqual(res.json(), json.loads(expect_res))


if __name__ == "__main__":
    unittest.main()
    print(issubclass(BaseCase,BaseCase))