import xlrd
import settings

class ExcleOperate:
    def __init__(self, sheet_index, file_path=settings.EXCEL_FILE):
        self.file_path = file_path
        self.sheet_index = sheet_index
        # 打开文件,获取一个book对象
        bookobj = xlrd.open_workbook(self.file_path)
        # bookobj.sheet_by_name(str) 获取名字获取对应的sheet
        # bookobj.sheet_by_index(int) int从0下标开始 获取excle对应下标的sheet
        self.sheet = bookobj.sheet_by_index(self.sheet_index)

    def get_excel(self):
        """
        获取excle数据
        :return: [{}, {}....]
        """
        temp = []

        # sheet.nrows 获取sheet页面有几行
        # sheet.ncols 获取sheet页面有几列
        for line in range(1, self.sheet.nrows):
            # sheet.row_values(int) int从0下标开始 获取sheet的第int行的值 返回一个列表
            temp.append(dict(zip(self.sheet.row_values(0), self.sheet.row_values(line))))

        return temp

if __name__ == '__main__':
    excle_data_list = ExcleOperate(0, settings.EXCEL_FILE).get_excel()
    print(excle_data_list)


    from jsonpath_rw import parse

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
    b = 'ywq[1].having'    # ywq[*].having 取全部
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

    import re
    import json

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