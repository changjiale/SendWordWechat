import requests
from bs4 import BeautifulSoup
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
}
def getword():
    '''
    获取一段暖话
    :return:
    '''
    user_url = 'http://www.ainicr.cn/qh/t83.html'
    resp = requests.get(user_url, headers=headers)
    soup_texts = BeautifulSoup(resp.text, 'lxml')
    # 『one -个』 中的每日一句
    num = random.randint(0,30)
    every_msg = soup_texts.find_all('div', class_='pbllists')[0].find_all('p')[num].text
    return every_msg
