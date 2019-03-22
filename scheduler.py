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
    #hour
    #scheduler.add_job(start_info, 'cron', hour=hour, minute=minute)
    # 每隔30秒发送一条数据用于测试。
    scheduler.add_job(start_info, 'interval', seconds=30)
    scheduler.start()

def start_info():

    city_name = friend_dict.get('city_name')
    start_date = time.mktime(time.strptime(friend_dict.get('start_date'),'%Y-%m-%d'))
    sweet_words = friend_dict.get('sweet_words')

    dictum_msg  = getword()
    mess = getWeather(city_name, start_date)

    today_mess = f'{mess}{dictum_msg}\n{sweet_words}\n'

    wechat_name = friend_dict['wechat_name']
    print(f'给 {wechat_name} 发送的内容是:\n{today_mess}')
    wechat = Wechat()
    if wechat.isonline(auto_login=True):
        name_uuid = wechat.getfriend().get("name_uuid")
        itchat.send(today_mess, name_uuid)
        #print(today_mess)
        #print(name_uuid)
    time.sleep(5)
    print('sucess')


def t():
    alarm_time = friend_dict['alarm_time']
    if alarm_time != '':


if __name__ == '__main__':
    scheduler()