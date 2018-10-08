# coding=utf-8

import logging

# 设定日志路径
logPath="../Log/log.log"

def initLogging():
    # 设定日志输出格式
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s [line:%(lineno)d] [ %(levelname)s ] %(message)s',
                        datefmt='%Y-%m-%d_%H:%M:%S',
                        filename=logPath,
                        filemode='a')

    # 设定日志轮转，最多备份5个日志文件，每个日志文件最大10M
    # BUG，logging不支持多进程，若进行轮转时候，将会导致无法进行更名情况
    # TODO：https://www.jianshu.com/p/d874a05edf19；重写FileHandler；暂时注释掉日志轮转设置
    # Rthandler = RotatingFileHandler(logPath, maxBytes=10 * 1024 * 1024, backupCount=10)
    # Rthandler.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # Rthandler.setFormatter(formatter)
    # logging.getLogger('').addHandler(Rthandler)
