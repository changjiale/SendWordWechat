# python+itchat定时发送当日天气情况和暖心话给指定微信好友(撩妹子哦)

## 项目运行

### 安装依赖

使用 pip install -r requirements.txt 安装所有依赖

### 项目运行
在setting.py中设置参数， 运行run.py的主方法即可(ps: 为方便操作可以在scheduler.py启动测试任务,发送间隔在30s方便测试)

## 项目介绍：
python+itchat自动发送暖心话给指定微信好友

### 项目地址
Github: [python+itchat自动发送暖心话给指定微信好友](https://github.com/changjiale/SendWordWechat) 

### 使用库
- [itchat](https://github.com/littlecodersh/ItChat) - 微信个人号接口
- [requests](http://docs.python-requests.org/en/master/) - 网络请求库
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#) - 解析网页
- [APScheduler](https://apscheduler.readthedocs.io/en/latest/) - 定时任务

### 功能
定时给女朋友发送每日天气、提醒、每日一句。

### 数据来源
暖心话来源  [情话网](http://www.ainicr.cn/qh/t83.html)

天气预报接口  http://t.weather.sojson.com/api/weather/city/+city_code (ps：citycode[下载地址](https://github.com/changjiale/SendWordWechat/blob/master/utils/city_code.json))


## 项目模块说明
utils

  -city_code.json #城市对应的citycode(编号)
  
  -jsonToDict.py  #将city.code.json中的城市名称和编号提取 存储到dict中
  
getwheater.py     #通过citycode 获取当天天气情况

getword.py        #获取一段暖言

wechat.py         #调用接口发送内容给微信指定好友

setting.py        #设置基本信息(好友名称, 定时任务时间， 所在城市， 相识时间， 最后留言等)

scheduler.py      #调用各模块，设置定时任务

run.py            #程序执行入口

## 项目效果
![命令行](https://github.com/changjiale/SendWordWechat/blob/master/demo.png)
![微信端](https://github.com/changjiale/SendWordWechat/blob/master/wechat.png)
## 最后呢，烦请各位看官，给个star呗

