import pytest
import json
import requests
from utils.ExcelOperation import ExcleOperate


# 0是login的sheet 1是warehouse
dic= ExcleOperate(1).get_excel_lists()
id_list = []

class TestWarehouse:



    def test_get_warehouses(self, login, data=dic[0]):
        headers = json.loads(data['header'])
        headers.update({'Authorization': login})
        # print(headers)
        resp = requests.request(method=data['method'],
                            url=data['url'],
                            headers=headers,
                            params=json.loads(data['para'])
                            )
        ret = resp.json()
        pytest.assume(ret.get('success'))


    def test_add_warehouse(self, login, data=dic[1]):
        headers = json.loads(data['header'])
        headers.update({'Authorization': login})
        # print(data[5])
        # body_data = json.dumps(data[5])
        resp = requests.request(method=data['method'],
                                url=data['url'],
                                headers=headers,
                                # data=json.loads(body_data).encode('utf-8').decode('latin-1')
                                data=data['body_data'].encode('utf-8').decode('latin-1')
                                )

        ret = resp.json()
        id = ret.get('data')
        id_list.append(id)
        print(id_list)
        pytest.assume(ret.get('success'))

    def test_edit_warehouse(self, login, data=dic[2]):
        headers = json.loads(data['header'])
        headers.update({'Authorization': login})
        body_data = json.loads(data['body_data'])
        id = id_list[-1]
        print(id)
        body_data.update({'id':id})
        resp = requests.request(method=data['method'],
                                url=data['url'],
                                headers=headers,
                                data=json.dumps(body_data).encode('utf-8').decode('latin-1')
                                )

        ret = resp.json()

        pytest.assume(ret.get('success') == True)


    def test_del_warehouse(self, login, data=dic[3]):
        headers = json.loads(data['header'])
        headers.update({'Authorization': login})
        id = id_list.pop()
        print(id_list, id)
        url = data.get('url').format(id=id)
        resp = requests.request(method=data['method'],
                                url=url,
                                headers=headers,
                                )

        ret = resp.json()
        pytest.assume(ret.get('success') == True)

