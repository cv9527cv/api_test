import json
import re
import requests
from jsonpath_rw import parse


class RequestsOperate:
    def __init__(self, current_case, all_excle_data_list):
        self.current_case = current_case
        self.all_excle_data_list = all_excle_data_list

    def get_response_msg(self):
         """
         发送请求并且获取结果
         """
         return self._send_msg()

    def _send_msg(self):
        """
        发送请求
        """
        a = self.current_case['method']
        print('method:  ', a, type(a))
        b = self._check_request_url()
        print('url:  ', b, type(b))
        c = self._check_request_headers()
        print('headers:  ', c, type(c))
        d = self._check_request_data()
        print('data:  ', d, type(d))
        e = self._check_request_json()
        print('json:  ', e, type(e))
        f = self._check_request_cookies()
        print('cookies:  ', f, type(f))
        response = requests.request(
            method=a,
            url=b,
            headers=c,
            data=d,
            json=e,
            cookies=f,
        )
        self._write_result(response)

        return response.json()

    def _check_request_url(self):
        url = self._operate_re_msg(self.current_case['url'])
        return url

    def _check_request_headers(self):
        headers = self.current_case['headers']
        if headers:
            # 变为字典
            headers = json.loads(self._operate_re_msg(headers))
        else:
            headers = {}
        return headers

    def _check_request_cookies(self):
        case_num = self.current_case['cookies']
        for item in self.all_excle_data_list:
            if item['case_num'] == case_num:
                return item['templation_response_cookies']
        else:
            return {}

    def _write_result(self, response):
        """
        将结果保存起来，供后面有依赖此结果的用例调用
        """
        for item in self.all_excle_data_list:
            if item['case_num'] == self.current_case['case_num']:
                # 以字典形式获取response返回的cookies, 写入cookies
                item['templation_response_cookies'] = response.cookies.get_dict()
                # 写入response json
                if response.headers['Content-Type'].lower() == 'application/json;charset=utf-8':
                    item['templation_response_json'] = response.json()
            # 这行代码把原来excle里的headers重新赋值给template_request_headers
            # 防止_operate_re_msg找request的依赖数据时找不到
            item['templation_request_headers'] = self.current_case['headers']
            item['templation_request_params'] = self.current_case['params']
            item['templation_request_data'] = self.current_case['data']

    def _check_request_data(self):
        """
        处理请求的data参数， 检查是否有依赖
        """
        data = self.current_case['data']
        if data:
            data = json.loads(self._operate_re_msg(data))
        else:
            data = {}
        return data

    def _check_request_json(self):
        """
        处理请求的data参数， 检查是否有依赖
        """
        send_json = self.current_case['json']
        if send_json:
            send_json = json.loads(self._operate_re_msg(send_json))
        else:
            send_json = {}
        return send_json

    def _operate_re_msg(self, parameter):
        """
        正则校验数据依赖的字段
        :param parameter:各种参数 如data：{‘token’: '$case01>response_json>data.token$'}
        """
        if not isinstance(parameter, str):
            parameter = json.dumps(parameter)
        pattern = re.compile(r'\$(.*?)\$')
        rule_list = pattern.findall(parameter)
        # 判断是否有数据依赖要处理
        if rule_list:
            for rule in rule_list:
                # 用例编号 列名（response_json, cookies等） json_path
                case_num, params, json_path = rule.split('>')
                for line in self.all_excle_data_list:
                    if line['case_num'] == case_num:
                        # 获取该列对应的值，比如{}
                        temp_data = line['templation_{}'.format(params)]
                        # json_path_rw 解析要求数据是字典
                        if isinstance(temp_data, str):
                            temp_data = json.loads(temp_data)
                        # 拿到规则
                        json_path_pattern = parse(json_path)
                        # 解析取值
                        match_list = json_path_pattern.find(temp_data)
                        if match_list:
                            match_data = str([v.value for v in match_list][0])
                            # 将提取出来的值替换原来的规则
                            parameter = re.sub(pattern=pattern, repl=match_data, string=parameter)
        return parameter



if __name__ == '__main__':
    data = {
        'ssm': {
            'age': '26',
            'salary': 12000
        },
        'pyy': {
            'age': 26,
            'salary': '12000'
        },
        'ywq': [
            {'having': 'flower'},
            {'having': 'smile'}
        ]
    }

    a = 'ssm.age'
    b = 'ywq[1].having'  # ywq[*].having 取全部
    my_parse_a = parse(a)
    my_parse_b = parse(b)
    my_find_a = my_parse_a.find(data)
    my_find_b = my_parse_b.find(data)
    print(my_find_a)
    for i in my_find_a:
        print(i.value)
    print(my_find_b)
    for i in my_find_b:
        print(i.value)

    sm = {'username': '$123>123>ssm.age$', 'pwd': '$erer>ewe>pyy.salary$', 'user': '$23>23>ywq[0].having$'}
    sm_json = json.dumps(sm)
    pattern = re.compile(r'\$(.*?)\$')
    re_find = pattern.findall(sm_json)
    print('11111111', re_find)
    for i in re_find:
        fei, wu, my_json_path = i.split('>')
        print(my_json_path)
        json_path_pattern = parse(my_json_path)
        result = json_path_pattern.find(data)
        temp = [i.value for i in result][0]
        print(temp)
        sm_json = re.sub(pattern, temp, sm_json, count=1)
        # break
    print(sm_json)