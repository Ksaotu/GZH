import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(receiver, title, body):
    mail_host="smtp.cnstrong.cn"  #设smtp置服务器
    mail_user="@cnstrong.cn"    #发送邮箱
    mail_pass=""   #授权码
    sender = '@cnstrong.cn'

    message = MIMEText(body, 'plain', 'utf-8')

    message['From'] = Header("乐桃学院接口测试报告", 'utf-8')
    message['To'] = Header("乐桃学院项目组", 'utf-8')

    subject = title
    message['Subject'] = Header(subject, 'utf-8')


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("无法发送邮件")

if __name__ == '__main__':
    send_email('eduplan@cnstrong.cn', '测试邮件', '查看')