import os
import datetime


# 配置文件
# ---------------------文件路径-----------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 读取的excle路径
EXCEL_FILE = os.path.join(BASE_DIR, r'static/api.xlsx')


#-----------------------allure报告--------------------

ALLURE_COMMAND= 'allure generate {from_path} -o {save_to_path} --clean'.format(
    from_path=os.path.join(BASE_DIR, 'report', 'json_result'),
    save_to_path=os.path.join(BASE_DIR, 'report', 'allure_result')
)

# ----------------------邮件相关---------------------
# 第三方 SMTP 服务
MAIL_HOST = "smtp.qq.com"  # 设置服务器   # 勿动
MAIL_USER = "ssm@qq.com"  # 用户名
MAIL_TOKEN = "XXXXXXXXXXX"  # 即授权码
# 设置收件人和发件人
SENDER = "ssm@qq.com"
# 接收邮件人列表
RECEIVERS = ["pyy@qq.com", "sun@qq.com"]

# 邮件主题
THEME = "物证溯源项目接口自动化测试报告"

# 邮件正文内容
SEND_CONTENT = "大家好，测试报告见附件。"

# 附件的file_name
SEND_FILE_NAME = "allure_report.zip"




# -----------------------日志相关--------------------
# 日志级别
LOG_LEVEL = 'debug'
LOG_STREAM_LEVEL = 'debug' # 屏幕输出流
LOG_FILE_LEVEL = 'info' # 文件输出流

# 日志文件命名
LOG_FILE_NAME = os.path.join(BASE_DIR, 'logs', datetime.datetime.now().strftime('%Y-%m-%d') + '.log')

