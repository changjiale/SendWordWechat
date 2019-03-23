from apscheduler.schedulers.blocking import BlockingScheduler
from getword import *
from setting import *
from getweather import *
import time, datetime
from wechat import Wechat
import itchat

def scheduler():
    # 定时任务
    scheduler = BlockingScheduler()
    # 每天规定时间发送
    alarm_time = friend_dict['alarm_time'].strip()

    #设置默认时间
    hour = 9
    minute = 30
    if alarm_time != '':
        list = alarm_time.split(':')
        hour = int(list[0])
        minute = int(list[1])
    #启动定时器
    scheduler.add_job(start_info, 'cron', hour=hour, minute=minute)
    # 每隔30秒发送一条数据用于测试。
    #scheduler.add_job(start_info, 'interval', seconds=30)
    scheduler.start()

#每次定时循环的任务
def start_info():
    #获取setting中信息
    city_name = friend_dict.get('city_name')
    wechat_name = friend_dict['wechat_name']
    #时间转化为时间戳
    start_date = time.mktime(time.strptime(friend_dict.get('start_date'),'%Y-%m-%d'))
    sweet_words = friend_dict.get('sweet_words')

    #获取一句话留言
    dictum_msg  = getword()
    mess = getWeather(city_name, start_date)

    #组成完整的一段话
    today_mess = f'{mess}{dictum_msg}\n{sweet_words}\n'

    print(f'给 {wechat_name} 发送的内容是:\n{today_mess}')

    #调用接口向指定好友发送
    wechat = Wechat()
    if wechat.isonline(auto_login=True):
        name_uuid = wechat.getfriend().get("name_uuid")
        itchat.send(today_mess, name_uuid)
    time.sleep(5)
    print('sucess')



