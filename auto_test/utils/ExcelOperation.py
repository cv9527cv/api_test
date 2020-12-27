import xlrd
import settings

class ExcleOperate:
    def __init__(self, sheet_index):
        self.sheet_index = sheet_index

    def get_excel_lists(self):
        bookobj = xlrd.open_workbook(settings.EXCEL_FILE)
        # 0是login的sheet 1是warehouse
        test_sheet = bookobj.sheet_by_index(self.sheet_index)

        temp = []
        for line in range(1, test_sheet.nrows):
            temp.append(dict(zip(test_sheet.row_values(0), test_sheet.row_values(line))))

        return temp

        # # 获取test_sheet的所有行的生成器
        # row_generator = test_sheet.get_rows()
        #
        # # 将生成器转化成列表[[cellobj, cellobj, ......], [..], [..], ......]，去除第一行
        # raw = list(row_generator)[1:]
        #
        # # 将列表从[[cellobj, cellobj, ..], ...]转换为[[str, str, ...], ...]
        # # temp: [[
        # # 'login_1',
        # # 'http://10.1.25.147:8889/login',
        # # 'post', {"Content-Length":"50", "Host":"10.1.25.147:8889"}, '',
        # # '{\n  "password": "123456",\n  "username": "ssm"\n}',
        # # '{"data":"XXXXX","success":true}',
        # # '登录接口，登录成功后返回的json数据中，data的值为token'
        # # ]....]
        # temp = []
        # for lis in raw:
        #     lis = list(map(lambda x:x.value, lis))
        #     temp.append(lis)
        # return temp