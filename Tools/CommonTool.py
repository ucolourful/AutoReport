# coding=utf-8

import os

def getHTMLStyle():
    """
    功能：获取邮件HTML样式
    :return:
    """
    css = "<style>" + \
           "H1 { font-size: x-large; color: red}" + \
           "H2 { font-size: large; color: blue ;}" + \
           "TABLE.test {border:1px #6595D6 solid; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px;background : snow}" + \
           "TD { font-size: 10pt; border:1px #6595D6 solid; border-top-width: 0px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 0px;}" + \
           "TH { background : skyblue;font-size: 10pt; border:1px #6595D6 solid; border-top-width: 0px; border-right-width: 1px; border-bottom-width: 1px; border-left-width: 0px;}" + \
           "TR { background :#F0F8FF}" + \
           "TR.PCO               { background : skyblue;color:blue}" + \
           "TR.PCO_FAIL          { background : skyblue;color:red}" + \
           "TR.PCO_AnotherFAIL   { background : skyblue;color:hotpink}" + \
           ".STAGE { background : lightsteelblue}" + \
           "TR.tableHeader  {background-color: #4455aa;color:white}" + \
           "TR.tableItem    {background-color: #C0C0C0}" + \
           "TR.Prompt  {color : blue}" + \
           "TR.Error   {color : red}" + \
           "TR.Debug   {color : darkgray}" + \
           "TR.Warning {color : deeppink}" + \
           "TR.message {color : green ; cursor : hand}" + \
           "td.Error   {color : red}" + \
           " a:link {" + \
           "    color:#000000;" + \
           "    text-decoration:underline;" + \
           "    }" + \
           "</style>"
    return css + "<body topmargin=\"0\" leftmargin=\"0\" marginheight=\"0\" marginwidth=\"0\">"

def parseConf(key = None,fileName = "projectConf"):
    """
    查询'key=value'键值对类型的配置文件
    :param key: 查询的关键字
    :param fileName: 配置文件名，默认projectConf
    :return: 返回key对应的value
    """

    # 设定返回值为None，若未找到key可返回value;若key为None，返回None
    value = None
    if key is None:
        return None

    # 获取当前路径
    curDir = os.path.dirname(os.path.abspath(__file__))

    # 判断文件是否存在，若不存在返回None
    if os.path.isfile(curDir + "//..//ProjectConf//" + fileName) is False:
        return None

    # 打开文件并获得key对应的value值
    file = open(curDir + "//..//ProjectConf//" + fileName, "r")
    for line in file.readlines():
        if line.split("=")[0] == key:
            value = line.split("=")[1].strip("\n")
    file.close()

    return value
