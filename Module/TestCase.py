# coding=utf-8

from xml.dom import minidom
import os

from datetime import datetime


def getCaseSitu():
    """
    获取用例执行简况
    :return:
    """
    caseInfoPath = "../Log/summary.xml"
    if os.path.isfile(caseInfoPath) is False:
        return None
    infoDoc = minidom.parse(caseInfoPath)
    fNode = infoDoc.firstChild
    testCaseInfo = {"caseCount":fNode.getAttribute("caseCount"), "failCount":fNode.getAttribute("failCount"), "testContinueTime":fNode.getAttribute("caseCount")}
    return testCaseInfo

def drawTcHTML(html):
    # 标题栏
    stepHTML = "\n<table width=\"90%\">"
    stepHTML += "\n<tr height=\"30\" class=\"tableHeader\">"
    stepHTML += "\n     <td colspan=\"7\" align=\"left\"><b><a name=\"gtr\">测试用例执行详情</a></b>"
    stepHTML += "\n </tr>"
    stepHTML += "\n <tr>"
    stepHTML += "\n    <td align=\"center\">测试套</td>"
    stepHTML += "\n    <td align=\"center\">测试用例</td>"
    stepHTML += "\n    <td align=\"center\">状态</td>"
    stepHTML += "\n    <td align=\"center\">开始时间</td>"
    stepHTML += "\n    <td align=\"center\">结束时间</td>"
    stepHTML += "\n    <td align=\"center\">耗时</td>"
    stepHTML += "\n    <td align=\"center\">原因</td>"
    stepHTML += "\n </tr>"

    # 解析日志文件，生成详情html
    caseInfoPath = "../Log/summary.xml"
    if os.path.isfile(caseInfoPath) is False:
        return None
    infoDoc = minidom.parse(caseInfoPath)
    fNode = infoDoc.firstChild
    suitSum = fNode.getElementsByTagName("TestSuit")
    if len(suitSum) > 0:
        for suitNode in suitSum:
            stepHTML += "\n <tr>"
            caseSum = suitNode.getElementsByTagName("TestCase")
            stepHTML += "\n    <td align=\"center\" rowspan=\"" + str(len(caseSum)) + "\">" + str(suitNode.getAttribute("name")) + "</td>"
            if len(caseSum) > 0:
                for i in range(0,len(caseSum)):
                    if i != 0:
                        stepHTML += "\n <tr>"
                    if str(caseSum[i].getAttribute("status")) == "success":
                        stepHTML += "\n    <td align=\"center\" bgcolor=\"green\">" + str(caseSum[i].getAttribute("name")) + "</td>"
                        stepHTML += "\n    <td align=\"center\" bgcolor=\"green\">" + str(caseSum[i].getAttribute("status")) + "</td>"
                    else:
                        stepHTML += "\n    <td align=\"center\" bgcolor=\"red\">" + str(caseSum[i].getAttribute("name")) + "</td>"
                        stepHTML += "\n    <td align=\"center\" bgcolor=\"red\">" + str(caseSum[i].getAttribute("status")) + "</td>"
                    stepHTML += "\n    <td align=\"center\">" + str(caseSum[i].getAttribute("startTime")) + "</td>"
                    stepHTML += "\n    <td align=\"center\">" + str(caseSum[i].getAttribute("endTime")) + "</td>"
                    startTime = datetime.strptime(str(caseSum[i].getAttribute("startTime")), '%Y-%m-%d %H:%M:%S')
                    endTime = datetime.strptime(str(caseSum[i].getAttribute("endTime")), '%Y-%m-%d %H:%M:%S')
                    stepHTML += "\n    <td align=\"center\">" + str(endTime - startTime) + "</td>"
                    stepHTML += "\n    <td align=\"center\">" + str(caseSum[i].getAttribute("reason")) + "</td>"
                    stepHTML += "\n </tr>"
                stepHTML += "\n </tr>"
    stepHTML += "\n</table ><br>"
    return html + stepHTML
