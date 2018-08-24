
# coding: utf-8

# In[1]:


import requests
import time
import random
import json


# In[2]:


#getting page data
def get_page(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.text
    return None

#parse page data
def parse_page(html):
    data = json.loads(html)['cmts']
    for item in data:
        yield{
        'date':item['time'].split(' ')[0],
        'nickname':item['nickName'],
        'city':item['cityName'],
        'score':item['score'],
        'content':item['content']
        }
#save
def save():
    for i in range(1,501):
        print(i)
        url = 'http://m.maoyan.com/mmdb/comments/movie/1175253.json?_v_=yes&offset='+str(i)
        html = get_page(url)
        for item in parse_page(html): 
            with open('爱情公寓.txt','a',encoding='utf-8') as f:
                f.write(item['date']+','+item['nickname']+','+item['city']+','+str(item['score'])+','+item['content']+'\n')
                time.sleep(1)
def clean_repeat(old, new):
    oldfile = open(old,'r',ecoding = 'utf-8')
    newfile = open(new,'w',ecoding = 'utf-8')
    content_list = oldfile.readlines()
    content_already = []
    for line in content_list:
        if line not in content_alread:
            newfile.write(line+'\n')
            content_alread.append(line)
            
if __name__ == '__main__':
    save()
    clean_repeat(r'爱情公寓_old.txt',r'爱情公寓_new.txt')

