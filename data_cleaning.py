# _*_ coding:utf-8 _*_
# @Author: masy
# @Date: 2022-03-17 19:48:03

import csv
import os


def cleanData(path):
    filename = os.path.basename(path)
    print(f'INFO - 正在清洗文件<{filename}>中的数据...')
    year = filename[9:13]
    saveDir = f'data2/{year}'
    os.makedirs(saveDir, exist_ok=True)
    saveFile = open(f'{saveDir}/{filename}', 'w', newline='', encoding='utf-8')
    writer = csv.writer(saveFile)
    
    openFile = open(path, 'r', encoding='utf-8')
    reader = csv.reader(openFile)
    i = 0
    for row in reader:
        if i == 0:
            row.insert(2, '最高气温')
            row[3] = '最低气温'
            writer.writerow(row)
            i += 1
        else:
            temperatures = row[2].split('/')
            row.insert(2, temperatures[0])
            row[3] = temperatures[1]
            writer.writerow(row)
    saveFile.close()
    openFile.close()
    print('INFO - 清洗数据完成！\n')

# 清洗data文件夹中的所有文件
#for folder, subfolders,filenames in os.walk('data'):
#    for filename in filenames:
#        cleanData(f'{folder}/{filename}')

path = 'data/2022/昭通历史天气预报_2022年4月份.csv'
cleanData(path)