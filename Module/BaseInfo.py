# coding=utf-8

def getBuildMsg():
    """
    获取构建概况，并返回数据
    :return: 返回构建概况(当前为测试数据)
    """
    res ={"testCaseInfo": None, "modOwners": None}
    testCaseInfo = {"caseCount": "99", "failCount": "1", "testContinueTime": "20:20:20"}
    modOwners = [{"module": "NULL", "owner": "NULL", "failCount": "0"}, {"module": "NULL", "owner": "NULL", "failCount": "0"}]
    res["testCaseInfo"] = testCaseInfo
    res["modOwners"] = modOwners
    return res

def drawBuildHTML(html):
    """
    获取到构建信息后，绘制报告html
    :param html: 传入html原始样式，并增加基础信息绘制
    :return:
    """
    msg = getBuildMsg()
    stepHTML = "\n<table width=\"50%\">"
    stepHTML += "\n<tr height=\"30\" class=\"tableHeader\">"
    # TODO，判定是冒烟还是全量
    stepHTML += "\n     <td colspan=\"4\" align=\"left\"><b><a name=\"gtr\">构建概况</a></b>"
    stepHTML += "\n </tr>"
    stepHTML += "\n <tr>"
    stepHTML += "\n    <td align=\"center\">验证项</td>"
    stepHTML += "\n    <td align=\"center\">结果</td>"
    stepHTML += "\n    <td align=\"center\">详细情况</td>"
    stepHTML += "\n    <td align=\"center\">失败特性及责任人</td>"
    stepHTML += "\n </tr>"
    stepHTML += "\n <tr>"
    stepHTML += "\n    <td align=\"center\">自动化</td>"
    # TODO，判定是通过还是不通过
    stepHTML += "\n    <td align=\"center\">通过</td>"
    # TODO，获取通过率
    stepHTML += "\n    <td align=\"left\">通 过 率：" + str(int(msg["testCaseInfo"]["caseCount"]) - int(msg["testCaseInfo"]["failCount"]) / int(msg["testCaseInfo"]["caseCount"])) + "% " \
                      "<br>脚本总数：" + str(msg["testCaseInfo"]["caseCount"]) + " " \
                      "<br>失败个数：" + str(msg["testCaseInfo"]["failCount"]) + " " \
                      "<br>构建时长：" + str(msg["testCaseInfo"]["testContinueTime"]) + "</td>"
    # TODO，获取开发人员
    userHTML = "\n<table >"
    userHTML += "\n <tr>"
    userHTML += "\n    <td align=\"center\">特性</td>"
    userHTML += "\n    <td align=\"center\">责任人</td>"
    userHTML += "\n    <td align=\"center\">失败个数</td>"
    userHTML += "\n </tr>"
    for modOwner in list(msg["modOwners"]):
        userHTML += "\n <tr>"
        userHTML += "\n    <td align=\"center\">" + modOwner["module"] + "</td>"
        userHTML += "\n    <td align=\"center\">" + modOwner["owner"] + "</td>"
        userHTML += "\n    <td align=\"center\" bgcolor=\"green\">" + modOwner["failCount"] + "</td>"
        userHTML += "\n </tr>"
    userHTML += "</table>"

    stepHTML += "\n    <td align=\"center\">" + userHTML + "</td>"
    stepHTML += "\n </tr>"
    stepHTML += "</table>"
    stepHTML += "\n</table ><br>"
    return html + stepHTML
