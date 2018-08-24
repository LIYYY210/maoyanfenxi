
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,STOPWORDS
from pyecharts import Geo,Style,Line,Bar,Overlap


# In[ ]:


f = open('爱情公寓.txt',encoding='utf-8')
data = pd.read_csv(f,sep=',',header=None, encoding='utf-8',names=['date','nickname','city','score','content'])
city = data.groupby(['city'])
score_group = city['score']
city_detail = city['score'].agg(['mean','count'])
city_detail.reset_index(inplace = True)
city_detail['mean'] = round(city_detail['mean'],2)   #average 

data_map = [(city_detail['city'][i], city_detail['count'][i]) for i in range(0,city_detail.shape[0])]
style = Style(title_color = "#BA55D3", title_pos = "center", width = 1500, height = 500, background_color="#BBFFFF")
geo = Geo("爱情公寓粉丝分布图", **style.init_style)
while True:
    try:
        attr,val = geo.cast(data_map)
        geo.add("",attr,val,visual_range=[0,20],visual_text_color="#BA55D3", symbol_size=20, is_visualmap=True, is_piecewise=True, visual_split_number=4)
    except ValueError as e:
        e = str(e)
        e = e.split("No coordinate is specified for")[1]
        for i in range(0,len(data_map)):
            if e in data_map[i]:
                daata_map.pop[i]
                break
    else:
        break
geo.render('爱情公寓.html')

city_main = city_detail.sort_values('count',ascending=False)[0:20]
attr = city_main['city']
v1 = city_main['count']
v2 = city_main['mean']
line = Line("主要城市评分")
line.add("城市",attr,v2,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
         mark_score=['min','max'], xaxis_interval=0, line_color='blue',
        line_width=5, mark_score_textcolor='black',mark_score_color='green', is_splitline_show=False)

bar = Bar("主要城市评论数")
bar.add("城市",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2, xaxis_interval=0, is_splitline_show=False)
overlap=Overlap()
overlap.add(bar)
overlap.add(line,yaxis_index=1, is_add_yaxis=True)
overlap.render('主要城市评分-平均分.html')

#comment = jieba.cut(str(data['comment']),cut_all=False)
#wl_space_split = " ".join(comment)

background_Image = plt.imread('map.jpg')
stopwords = STOPWORDS.copy()
wc = WordCloud(width=1000,height=800,background_color="#FFFFFF", mask=background_Image,front_path="C:\aqgy.ttf",
               stopwords=stopwords,max_font_size=400,random_state=50)
wc.generate_feom_text(wl_space_split)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file(r'aqgy.jpg')

