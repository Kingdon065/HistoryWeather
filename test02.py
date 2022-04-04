# _*_ coding:utf-8 _*_
# @Author: DarkKing
# @Date: 2022-04-03 22:50:33

import os

for folder,subfolders,filenames in os.walk('data'):
    for filename in filenames:
        path = os.path.join(folder, filename)
        os.system(f"cvtecd {path} -e utf-8 -o")