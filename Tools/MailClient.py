#coding=UTF-8

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class MailClient:
    def __init__(self):
        """SMTP发送服务器地址"""
        self._smtpServer='smtpscn.colorful.com'
        "登录邮件服务器使用的邮件账号"
        self._smtpUser='storhardwareci@colorful.com'
        "登录邮件服务器使用的邮件账号密码"
        self._smtpPwd='Storage12#$'
        "默认服务器监听端口"
        self._smtpPort='25'
        self._mailServer=smtplib.SMTP(self._smtpServer,self._smtpPort)
        self._mailServer.login('pmail_StorHardwareCI', self._smtpPwd)
        self._mailServer.ehlo()
        
    def Send(self, Subject, Content, user):
        msg = MIMEMultipart('related')
        msg['Subject'] = Subject
        
        
        msg['From'] = self._smtpUser

        msg['To'] = ",".join(["%s@notesmail.colorful.com" % TmpUser for TmpUser in user])

        msg.preamble = 'This is a multi-part message in MIME format.' 
        msgAlternative = MIMEMultipart('alternative')
        msg.attach(msgAlternative)
    
        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)
        
        # We reference the image in the IMG SRC attribute by the ID we give it below
        msgText = MIMEText(Content, 'html','utf-8')
        msgAlternative.attach(msgText)

        try:
            for TmpUser in user:
                #yuping
                msg['bcc'] = TmpUser
                #end
                self._mailServer.sendmail(self._smtpUser, TmpUser + "@notesmail.colorful.com", msg.as_string())
                #print "send mail to %s success!" % TmpUser
        except Exception,ex:
            print Exception,ex
            print 'mail exception -> send failed'
            self._mailServer=smtplib.SMTP(self._smtpServer,self._smtpPort)
            self._mailServer.ehlo() 
            for TmpUser in user:
                #yuping
                msg['bcc'] = TmpUser
                #end
                print 'TmpUser =', TmpUser
                self._mailServer.sendmail(self._smtpUser, TmpUser + "@notesmail.colorful.com", msg.as_string())
        else:
            print "send mail success!"
        
    def Release(self):
        self._mailServer.quit()

if __name__=="__main__":
    Mail=MailClient()
    Mail.Send("test..【SELF TEST】", "testing",["506231730@qq.com"])
    Mail.Release()
    
