#coding=UTF-8

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class MailClient:
    def __init__(self):
        """SMTP发送服务器地址"""
        self._smtpServer='smtp.qq.com'
        "登录邮件服务器使用的邮件账号"
        self._smtpUser='2652887095@qq.com'
        "登录邮件服务器使用的邮件账号密码"
        self._smtpPwd='xdgtgycmtqujdjid'
        "默认服务器监听端口"
        self._smtpPort='465'
        self._mailServer=smtplib.SMTP_SSL(self._smtpServer,self._smtpPort)
        self._mailServer.login(self._smtpUser, self._smtpPwd)
        
    def Send(self, Subject, Content, user):
        msg = MIMEMultipart('related')
        msg['Subject'] = Subject
        msg['From'] = self._smtpUser
        msg['To'] = ",".join([TmpUser for TmpUser in user])

        msg.preamble = 'This is a multi-part message in MIME format.'
        msgAlternative = MIMEMultipart('alternative')
        msg.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        msgText = MIMEText(Content, 'html','utf-8')
        msgAlternative.attach(msgText)

        try:
            for TmpUser in user:
                self._mailServer.sendmail(self._smtpUser, TmpUser, msg.as_string())
        except Exception,ex:
            print Exception,ex
            print 'mail exception -> send failed'
            self._mailServer=smtplib.SMTP(self._smtpServer,self._smtpPort)
            for TmpUser in user:
                self._mailServer.sendmail(self._smtpUser, TmpUser, msg.as_string())
        else:
            print "send mail success!"
        
    def Release(self):
        self._mailServer.quit()

if __name__=="__main__":
    Mail=MailClient()
    Mail.Send("test..【SELF TEST】", "testing",["506231730@qq.com"])
    Mail.Release()