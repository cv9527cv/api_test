import pytest
from utils.AllureHandler import AllureOperate
from settings import LOG_FILE_NAME

import logging

logging.basicConfig(
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    level=20,
    filename=LOG_FILE_NAME,
    filemode='w'
)


if __name__ == '__main__':
    pytest.main()
    # 生成报告，发送邮件
    allure_0bj = AllureOperate()
    allure_0bj.get_allure_report()
    allure_0bj.send_mail()