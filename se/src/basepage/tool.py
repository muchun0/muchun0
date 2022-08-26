import datetime
import os
import time

import requests


def writeData(movie_name,url:list,data):
    for i in url:
        try:
            pic_data = requests.get(i).content
            time.sleep(3)
            # 创建影片名文件夹
            if not os.path.exists(r'C:\Users\11203\Desktop\pic\\' + str(datetime.date.today()) + f'\\{movie_name}'):
                os.mkdir(r'C:\Users\11203\Desktop\pic\\' + str(datetime.date.today()) + f'\\{movie_name}')
            pic_os_path = r'C:\Users\11203\Desktop\pic\\' + str(datetime.date.today()) + f'\\{movie_name}' + f'\\{movie_name}.jpg'
            with open(pic_os_path,'wb') as file:
                file.write(pic_data)
            movie_data_path = r'C:\Users\11203\Desktop\pic\\' + str(
                            datetime.date.today()) + f'\\{movie_name}' + f'\\{movie_name}.txt'
            with open(movie_data_path, 'w', encoding='utf-8') as f:
                        f.write(data)
        except:
            pass