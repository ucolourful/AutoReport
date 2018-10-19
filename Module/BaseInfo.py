# coding=utf-8

from Module.TestCase import getCaseSitu

def getBuildMsg():
    """
    获取构建概况，并返回数据
    :return: 返回构建概况(当前为测试数据)
    """
    res ={"testCaseInfo": None, "modOwners": None}
    testCaseInfo = getCaseSitu()
    modOwners = [{"module": "module1", "owner": "user1", "failCount": "0"}, {"module": "module2", "owner": "user2", "failCount": "1"}]
    res["testCaseInfo"] = testCaseInfo
    res["modOwners"] = modOwners
    return res

def drawBuildHTML(html, runMode):
    """
    获取到构建信息后，绘制报告html
    :param html: 传入html原始样式，并增加基础信息绘制
    :return:
    """
    msg = getBuildMsg()
    stepHTML = "\n<table width=\"50%\">"
    stepHTML += "\n<tr height=\"30\" class=\"tableHeader\">"
    if runMode == "Roll":
        stepHTML += "\n     <td colspan=\"4\" align=\"left\"><b><a name=\"gtr\">冒烟构建概况</a></b>"
    elif runMode == "All":
        stepHTML += "\n     <td colspan=\"4\" align=\"left\"><b><a name=\"gtr\">全量构建概况</a></b>"
    stepHTML += "\n </tr>"
    stepHTML += "\n <tr>"
    stepHTML += "\n    <td align=\"center\">验证项</td>"
    stepHTML += "\n    <td align=\"center\">结果</td>"
    stepHTML += "\n    <td align=\"center\">详细情况</td>"
    stepHTML += "\n    <td align=\"center\">失败模块及责任人</td>"
    stepHTML += "\n </tr>"
    stepHTML += "\n <tr>"
    stepHTML += "\n    <td align=\"center\">自动化</td>"
    # 冒烟要求100%通过率才是通过；全量要求99%以上才算通过
    if runMode == "Roll" and int(msg["testCaseInfo"]["caseCount"]) - int(msg["testCaseInfo"]["failCount"]) / int(msg["testCaseInfo"]["caseCount"]) >= 100:
        stepHTML += "\n    <td align=\"center\">通过</td>"
    elif runMode == "Roll" and int(msg["testCaseInfo"]["caseCount"]) - int(msg["testCaseInfo"]["failCount"]) / int(msg["testCaseInfo"]["caseCount"]) < 100:
        stepHTML += "\n    <td align=\"center\">不通过</td>"
    elif runMode == "All" and int(msg["testCaseInfo"]["caseCount"]) - int(msg["testCaseInfo"]["failCount"]) / int(msg["testCaseInfo"]["caseCount"]) >= 99:
        stepHTML += "\n    <td align=\"center\">通过</td>"
    elif runMode == "All" and int(msg["testCaseInfo"]["caseCount"]) - int(msg["testCaseInfo"]["failCount"]) / int(msg["testCaseInfo"]["caseCount"]) < 99:
        stepHTML += "\n    <td align=\"center\">不通过</td>"
    stepHTML += "\n    <td align=\"left\">通 过 率：" + str(int(msg["testCaseInfo"]["caseCount"]) - int(msg["testCaseInfo"]["failCount"]) / int(msg["testCaseInfo"]["caseCount"])) + "% " \
                      "<br>用例总数：" + str(msg["testCaseInfo"]["caseCount"]) + " " \
                      "<br>失败个数：" + str(msg["testCaseInfo"]["failCount"]) + " " \
                      "<br>构建时长：" + str(msg["testCaseInfo"]["testContinueTime"]) + "</td>"
    userHTML = "\n<table >"
    userHTML += "\n <tr>"
    userHTML += "\n    <td align=\"center\">模块</td>"
    userHTML += "\n    <td align=\"center\">责任人</td>"
    userHTML += "\n    <td align=\"center\">失败个数</td>"
    userHTML += "\n </tr>"
    for modOwner in list(msg["modOwners"]):
        userHTML += "\n <tr>"
        userHTML += "\n    <td align=\"center\">" + modOwner["module"] + "</td>"
        userHTML += "\n    <td align=\"center\">" + modOwner["owner"] + "</td>"
        if int(modOwner["failCount"]) == 0:
            userHTML += "\n    <td align=\"center\" bgcolor=\"green\">" + modOwner["failCount"] + "</td>"
        else:
            userHTML += "\n    <td align=\"center\" bgcolor=\"red\">" + modOwner["failCount"] + "</td>"
        userHTML += "\n </tr>"
    userHTML += "</table>"
    stepHTML += "\n    <td align=\"center\">" + userHTML + "</td>"
    stepHTML += "\n </tr>"
    stepHTML += "</table>"
    stepHTML += "\n</table ><br>"
    return html + stepHTML
