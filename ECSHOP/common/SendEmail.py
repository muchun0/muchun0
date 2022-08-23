# coding:UTF-8
# 计算机名字不能是中文
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
class SendEmail():
    def sendEmail(self,filepath):
        #声明邮箱服务器地址
        smtpserver = 'smtp.qq.com'
        #声明163邮箱用户名
        username = '1120305692@qq.com'
        #声明该用户授权码,不是邮箱密码,而是IMAP/SMTP服务授权码
        password = 'pllxivktqybiggfa'
        #表明发件人
        sender = '1120305692@qq.com'
        #声明收件人
        receiver = ['1078540244@qq.com','1411277075@qq.com']
        #邮件主题
        subject = '接口测试报告'
        msg = MIMEMultipart('mixed')
        # 邮件正文
        msg.attach(MIMEText('God bless you！'))
        msg['Subject'] = subject
        msg['From']= '1120305692@qq.com <1120305692@qq.com>'
        #声明邮件接收人有两种方式，第一种是固定receiver指定的人接收
        #msg['To'] = receiver
        #第二种可以由多个人接收，每个收件人之间用逗号隔开
        msg['To'] = ':'.join(receiver)
        #给邮箱添加附件,b代表二进制，r代表读，即以二进制方式读取文件
        f = open(filepath,'rb')
        sendfile = f.read()
        f.close()
        text_att = MIMEText(sendfile,'base64','utf-8')
        text_att['Content-Type'] = 'application/octet-stream'
        #给文本添加标题
        text_att.add_header('Content-Disposition','attachment',filename = 'report.html')
        msg.attach(text_att)
        #发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username,password)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
if __name__ == '__main__':
    #调用发送邮件
    SendEmail().sendEmail()