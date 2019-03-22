from utils.jsonToDict import JsonDict
import requests
import json
from datetime import datetime
import time

def getWeather(city_name="北京", start_stamp=1514736000,dictum_msg='傻子多吃点',sweet_words='来自最爱你的我'):
    city_codes = JsonDict().jsonToDict()
    city_code = city_codes[city_name]
    url = "http://t.weather.sojson.com/api/weather/city/"+city_code
    print(url)
    response = requests.get(url)
    #print(response.status_code)
    if response.status_code == 200 and response.json()['status']==200:
        weather =  response.json()
        #位置
        location = weather['cityInfo']['parent']+weather['cityInfo']['city']
        #当前时间
        today_time = datetime.now().strftime('%Y{y}%m{m}%d{d}').format(y='年',m='月',d='日')
        # 今日天气
        today_weather = weather.get('data').get('forecast')[0]
        #print(today_weather)
        # 今日天气注意事项
        notice = today_weather.get('notice')
        #当前状况
        #print(weather.get('data').get("wendu"))
        nowtemperature = f'     温度 : {weather.get("data").get("wendu")}℃'
        nowshidu = f'湿度 : {weather.get("data").get("shidu")}'
        nowpm25 = f'PM2.5 : {weather.get("data").get("pm25")}'

        # 温度
        high = today_weather.get('high')
        high_c = high[high.find(' ') + 1:]
        low = today_weather.get('low')
        low_c = low[low.find(' ') + 1:]
        temperature = f"温度 : {low_c}~~{high_c}"
        # 风
        fx = today_weather.get('fx')
        fl = today_weather.get('fl')
        wind = f"{fx} : {fl}"
        # 空气指数
        aqi = today_weather.get('aqi')
        aqi = f"空气 : {aqi}"
        # 相识多少天了
        know_days = int ((time.time()-start_stamp)/86400)
        tell_msg = f'猪猪啊， 这是我们相识的第 {know_days} 天'

        today_msg = f'{today_time}\n{tell_msg}。\n当前天气状况 : \n{nowtemperature}, {nowshidu}, {nowpm25}\n{notice}\n{temperature}\n{wind}\n{aqi}\n{dictum_msg}\n{sweet_words}\n'
        return today_msg









if __name__ == '__main__':
    print(getWeather("洛阳"))
