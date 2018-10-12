# coding=utf-8

from Module.Package import drawPkgHTML
from Tools.CommonTool import getHTMLStyle
from Tools.LOGTool import initLogging
import logging
from Tools.MailClient import MailClient


def initConfig():
    """
    初始化全局配置
    :return: NONE
    """
    # 初始化日志输出工具
    initLogging()
    logging.info("---Step1: init the logging config")


def analysisLogAndDrawReport():
    """
    分析日志并绘制报告格式
    :return: HTML(已经绘制over的HTML)
    """
    logging.info("---Step2: get HTML style")
    HTML = getHTMLStyle()

    logging.info("---Step3: analysis project logs and draw report")
    HTML = drawPkgHTML(HTML)
    return HTML + "</body>"

def sendReport(HTML):
    """
    发送报告
    :param HTML: 已经绘制好的HTML
    :return:
    """
    logging.info("---Step4: send report to people")
    Mail = MailClient()
    Mail.Send("test..【SELF TEST】", HTML, ["lwx513980"])
    Mail.Release()

if __name__ == "__main__":
    # 初始化全局配置
    initConfig()

    # 分析日志并绘制报告格式
    HTML = analysisLogAndDrawReport()

    # 发送报告
    sendReport(HTML)

    # 日志刷新正常结束标记
    logging.info("---Step5: normal ending")
