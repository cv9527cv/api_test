import pytest
import requests
import sys

import os.path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from utils import ExcelOperation
import json



@pytest.fixture(scope='session')
def login():
    dic = ExcelOperation.ExcleOperate(0).get_excel_lists()[0]
    resp = requests.request(method=dic['method'],
                            url=dic['url'],
                            headers=json.loads(dic['header']),
                            data=json.loads(json.dumps(dic['body_data']))
                            )
    ret = resp.json()

    sign = ret.get('success')
    token = ret.get('data')

    if sign:
        token = 'Bearer ' + token
        return token

