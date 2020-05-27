'''
@Time  : 2020/4/14 14:51
@Author: fengzhj
@doc   : 请求YAPI服务端测试，返回测试结果，并发送邮件
'''
import requests
from .emails import send_email
import os
from .emails import send_msg


receiver = []  # 收件人列表
body1 = '20.2环境有接口用例测试未通过，请登录YAPI测试相关接口：http://192.168.20.146:3000/project/517/interface/col/518 \n '
pass_body1 = '20.2环境接口回归通过 \n '
body3 = '\n用例ID      用例名称             接口地址                  测试结果 \n'

url = "http://192.168.20.146:3000/api/open/run_auto_test"

class YapiTest():
    """获取测试结果并保存到文件中"""
    failed_list = []  # 错误测试用例数量
    caseNum_list = []  # 用例总数
    failcase_list = []  # 错误用例
    failcase_num = 0
    allcase_num = 0

    def yapi_test(self, list_case):  # 传入测试id列表
        for case_num in list_case:
            querystring = {"id": str(case_num), "token": "ebe5af1cd8346f601c13", "mode": "json", "email": "false",
                           "download": "false"}
            response = requests.request("GET", url, params=querystring).json()
            # print(response)
            self.failed_list.append(response["message"]["failedNum"])
            self.caseNum_list.append(response["message"]["len"])

            self.failcase_list.extend(response["list"])

        self.failcase_num = sum(self.failed_list)
        self.allcase_num = sum(self.caseNum_list)

        # 错误用例总数
        # 错误结果写入文本
        with open('failcase_list', 'a', encoding='utf-8') as f:
            for case in self.failcase_list:
                if case['code'] == 1:
                    failcase = case['id'], case['name'], case['path'], case['validRes']
                    f.write(str(failcase) + "\n")
        # 通过用例写入文本
        with open('passcase_list', 'a', encoding='utf-8') as f:
            for case in self.failcase_list:
                if case['code'] == 0:
                    failcase = case['id'], case['name'], case['path'], case['validRes']
                    f.write(str(failcase) + "\n")


    def send(self):
        """发送邮件"""
        if self.failcase_num != 0:
            title = '有' + str(self.failcase_num) + '个接口用例回归未通过，请关注并及时处理'
            body2 = '用例总数：' + str(self.allcase_num) + ' \n 失败用例数：' + str(self.failcase_num) + ' \n以下是失败用例信息： \n'
            with open('failcase_list', 'r', encoding='utf-8') as b:
                body = body1 + body2 + body3 + b.read()
                # print(body)
            send_msg(title + body)
            send_email(receiver, title, body)
        else:
            pass_title = '所有用例回归通过!'
            pass_body2 = '用例总数：' + str(self.allcase_num) + ' \n以下是用例信息： \n'
            with open('passcase_list', 'r', encoding='utf-8') as b:
                pass_body = pass_body1 + pass_body2 + body3 + b.read()
            # send_msg(pass_title + pass_body)
            send_email(receiver, pass_title, pass_body)

    def del_result(self):
        path = './failcase_list'  # 文件路径
        if os.path.exists('./failcase_list'):
            os.remove('./failcase_list')
            print("文件删除成功")

        if os.path.exists('./passcase_list'):
            os.remove('./passcase_list')
            print("文件删除成功")