import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json
import requests

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
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("无法发送邮件")

def send_msg(msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at": {
            "atMobiles": [],  # 此处为需要@什么人。填写具体用户
            "isAtAll": False  # 此处为是否@所有人
        }
    }
    url = 'https://oapi.dingtalk.com/robot/send?access_token='
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

'''
def send_msg(title, body):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "link",
        "link": {
            "title": title,
            "text": body,
            "messageUrl": "http://192.168.24.123:8080/view/LT_college/job/LT_college/allure/"
        }
    }
    url = 'https://oapi.dingtalk.com/robot/send?access_token='
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text
'''

if __name__ == '__main__':
    # send_email('eduplan@cnstrong.cn', '测试邮件', '查看')
    send_msg('所有接口用例回归通过')