# coding=utf-8
from Module.BaseInfo import drawBuildHTML
from Module.Package import drawPkgHTML
from Module.TestCase import drawTcHTML
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


def analysisLogAndDrawReport(runMode):
    """
    分析日志并绘制报告格式
    :return: HTML(已经绘制over的HTML)
    """
    logging.info("---Step2: get HTML style")
    HTML = getHTMLStyle()

    logging.info("---Step3: analysis project logs and draw report")

    # step 3.1 ：绘制构建情况
    HTML = drawBuildHTML(HTML, runMode)

    # step 3.2 ：绘制出包信息
    HTML = drawPkgHTML(HTML, runMode)

    # step 3.3 ：绘制用例信息
    HTML = drawTcHTML(HTML)
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

    # 分析日志并绘制报告格式(runMode为构建方式，Roll=冒烟、All=全量)
    HTML = analysisLogAndDrawReport(runMode="Roll")

    # 发送报告
    sendReport(HTML)

    # 日志刷新正常结束标记
    logging.info("---Step5: normal ending")
