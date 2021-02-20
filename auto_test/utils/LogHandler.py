import logging

if __name__ == "__main__":
    # 创建一个loggering对象
    logger = logging.getLogger()

    # 创建一个文件对象，输出到文件
    fh = logging.FileHandler('标配版.log', encoding='utf-8')

    # 创建一个屏幕对象，即输出到控制台
    sh = logging.StreamHandler()

    # 配置显示格式
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

    # 绑定格式
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    # loggering对象绑定fh 和 sh
    logger.addHandler(fh)
    logger.addHandler(sh)

    # 总开关 默认30 优先级比fh和sh高 即先过滤总开关  再过滤sh 和 fh
    logger.setLevel(10)

    # fh和sh两个对象分别设置开关
    fh.setLevel(10)
    sh.setLevel(40)
