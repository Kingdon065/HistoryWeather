# _*_ coding:utf-8 _*_
# @Author: masiy
# @Date: 2022-03-14 20:07:43

import os
import bs4
import requests
import csv
import time
from random import randint
from Color.color import Colored

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

class HistoryWeather:
    def __init__(self, url) -> None:
        res = requests.get(url, headers=headers)
        self.soup = bs4.BeautifulSoup(res.text, 'lxml')
    
    def getData(self):
        self.color = Colored()
        div_tag = self.soup.select_one("div[class='wdetail']")
        title = div_tag.select_one("h1")
        title = title.text.strip().replace(' ', '_')
        print(self.color.lightyellow(f'INFO - 正在抓取<{title}>...'))
        save_dir = f'data/{title[9:13]}'
        os.makedirs(save_dir, exist_ok=True)
        f = open(f"{save_dir}/{title}.csv", 'w', newline='', encoding='utf-8')
        writer = csv.writer(f)
        
        for tr_tag in div_tag.select("tr"):
            row = []
            for td_tag in tr_tag.select("td"):
                data = td_tag.text.strip().replace(' ', '').replace('\r\n', '')
                row.append(data)
            writer.writerow(row)
        
        f.close()
        print(self.color.lightgreen('INFO - 抓取成功！'))


if __name__ == '__main__':
    s = time.localtime()
    cur_year = s.tm_year
    cur_month = s.tm_mon
    
    start_year = 2022
    start_month = 4
    
    while True:
        if start_year == cur_year:
            if start_month > cur_month:
                break
        if start_month > 12:
            start_year += 1
            start_month = 1
        if start_year > cur_year:
            break
        
        print('INFO - 正在启动抓取程序...')
        url = f'http://www.tianqihoubao.com/lishi/zhaotong/month/{start_year}{start_month:02d}.html'
        hw = HistoryWeather(url)
        hw.getData()
        start_month += 1
        # 随机等待
        secs = randint(3, 10)
        print(hw.color.lightred(f'INFO - 抓取程序暂停{secs}秒...\n'))
        time.sleep(secs)