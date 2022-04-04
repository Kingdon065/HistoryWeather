# _*_ coding:utf-8 _*_
# @Author: masy
# @Date: 2022-03-31 22:07:23

import os
import csv


def get_history_days(month, day, folder='data2'):
    mon_keyword = f'{month}月份'
    title = True
    for year_folder in sorted(os.listdir(folder)):
        year_folder = os.path.join(folder, year_folder)
        for filename in os.listdir(year_folder):
            if mon_keyword in filename:
                path = os.path.join(year_folder, filename)
                f = open(path)
                reader = csv.reader(f)
                data = list(reader)
                if title:
                    print(f'{data[0][0]:20}{data[0][2]:5}{data[0][3]:5}')
                    title = False
                print(f'{data[day][0]:20}{data[day][2]:10}{data[day][3]:10}')
                f.close()


get_history_days(5, 1)
                    