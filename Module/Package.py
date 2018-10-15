# coding=utf-8

import logging
import os
import time

from Tools.CommonTool import parseConf


def getPkgInfoList():
    """
    获取包信息
    :return: [['pkgName1','date1'],['pkgName2','date2']]
    """
    pkgInfoList = []
    logging.info("---Step3.2: get package info")
    pkgPath = parseConf("pkgPath")

    # 防止未取到信息的情况下继续运行
    if pkgPath is None or pkgPath == "":
        logging.error("---Step3.2.1: get package path error; pkgPath not exist")
        raise Exception("fail to get package path; pkgPath not exist")
    logging.info("---Step3.2.1: get package path ok; pkgPath = %s" % pkgPath)

    # 判断获取的路径是否存在
    if os.path.exists(pkgPath) is False:
        return None

    # 获取所有包，并记录到日志中
    logging.info("---Step3.2.2: get package list:")
    for root, dirs, files in os.walk(pkgPath):
        for file in files:
            if os.path.splitext(file)[1] == ".tgz":
                logging.info("---Step3.2.2.pkg: %s  %s" % (file, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(root + "\\" + file)))))
                pkgInfo = [file, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(root + "\\" + file)))]
                pkgInfoList.append(pkgInfo)
    return pkgInfoList

def drawPkgHTML(html):
    """
    获取到包信息后，进行绘制报告HTML
    :param html: 传入html原始样式，并增加包信息绘制
    :return: html: 原始html+包信息html
    """
    pkgInfoList = getPkgInfoList()
    pkgHtml = "\n<table width=\"50%\">"
    pkgHtml += "\n<tr height=\"30\" class=\"tableHeader\">"
    pkgHtml += "\n     <td colspan=\"2\" align=\"left\"><b><a name=\"gtr\">出包信息</a></b>"
    pkgHtml += "\n </tr>"
    pkgHtml += "\n <tr>"
    pkgHtml += "\n    <td align=\"center\">名称</td>"
    pkgHtml += "\n    <td align=\"center\">时间</td>"
    pkgHtml += "\n </tr>"
    for pkgInfo in list(pkgInfoList):
        pkgHtml += "\n <tr>"
        pkgHtml += "\n    <td align=\"center\">" + pkgInfo[0] + "</td>"
        pkgHtml += "\n    <td align=\"center\">" + pkgInfo[1] + "</td>"
        pkgHtml += "\n </tr>"
    pkgHtml += "\n</table ><br>"
    return html + pkgHtml
