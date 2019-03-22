import itchat
from setting import *
'''
通过二维码登录微信，判断登录状态，定位好友
'''
class Wechat():

    '''
    初始化
    '''
    def __init__(self):
        self.friend_name = friend_dict['wechat_name']
        self.alarm_hour = friend_dict['alarm_time']

    def isonline(self, auto_login=False):
        '''
        判断登录
        :param auto_login:
        :return:
        '''
        def online():
            '''
            通过获取好友信息，判断用户是否还在线
            :return: True ，还在线，False
            不在线了
            '''
            try:
                if itchat.search_friends():
                    return True
            except:
                return False
            return True

        if online():
            return True
        # 仅仅判断是否在线
        if not auto_login:
            return online()

        # 登陆，尝试 5 次
        for _ in range(5):
            # 命令行显示登录二维码
            # itchat.auto_login(enableCmdQR=True)
            itchat.auto_login()
            if online():
                print('登录成功')
                return True
        else:
            print('登录成功')
            return False

    def getfriend(self):
        '''
        获取指定好友
        :return:   好友uuid
        '''
        if not self.isonline(True):
            return
        friend = itchat.search_friends(name=self.friend_name)
        if not friend:
            print('昵称错误')
            return
        name_uuid = friend[0].get('UserName')
        friends={}
        friends['name_uuid'] = name_uuid
        return friends
