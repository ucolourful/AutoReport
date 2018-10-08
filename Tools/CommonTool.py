# coding=utf-8

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
    return css
