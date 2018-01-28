import time 

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('115.159.147.80',27017)
songs = client.kugou_db.songs

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,"lxml")
    ranks = soup.select(".pc_temp_num")
    titles = soup.select(".pc_temp_songlist > ul > li > a")
    song_times = soup.select(".pc_temp_time")

    for rank,title,song_time in zip(ranks,titles,song_times):
        data = {
            'rank': rank.get_text().strip(),
            'singer': title.get_text().split('-')[0].strip(),
            'song': title.get_text().split('-')[1].strip(),
            'time': song_time.get_text().strip(), 
        }

        print(data)
        song_id = songs.insert(data)
        print(song_id)
        print('----------------------------')

if __name__ == "__main__":
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1,24)]
    for url in urls:
       get_info(url)
       time.sleep(1)
          

