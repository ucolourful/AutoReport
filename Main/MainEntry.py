# coding=utf-8

from Tools.LOGTool import initLogging
import logging

def init():
    """
    初始化全局配置
    :return: NONE
    """
    # 初始化日志输出工具
    initLogging()

if __name__ == "__main__":
    init()
    logging.error("test")
