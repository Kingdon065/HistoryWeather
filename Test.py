# _*_ coding:utf-8 _*_
# @Author: masy
# @Date: 2022-03-18 12:21:05

import os
import shutil

f = 'data/ret.txt'

print(os.path.basename(f))

for filename in os.listdir('data'):
    source = os.path.join('data', filename)
    if os.path.isdir(source):
        continue
    save_dir = f'data/{filename[9:13]}'
    os.makedirs(save_dir, exist_ok=True)
    dist = os.path.join(save_dir, filename)
    print(f'INFO - 正在将{source}移动到{dist}...')
    shutil.move(source, dist)

