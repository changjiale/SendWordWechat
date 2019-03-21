from utils.jsonToDict import JsonDict
import requests
import json
import datetime

def getWeather(city_name="北京"):
    city_codes = JsonDict().jsonToDict()
    city_code = city_codes[city_name]
    url = "http://t.weather.sojson.com/api/weather/city/"+city_code
    print(url)
    response = requests.get(url)
    #print(response.status_code)
    if response.status_code == 200 and response.json()['status']==200:
        weather =  response.json()
        for key, value in weather.items():
            print(key," : ",value)
        #位置
        location = weather['cityInfo']['parent']+weather['cityInfo']['city']
        #当前时间
        today_time = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')





if __name__ == '__main__':
    getWeather("洛阳")
