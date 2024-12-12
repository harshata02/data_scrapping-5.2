

import requests as rq

from bs4 import BeautifulSoup
import pandas as pd



newsUrl ='https://www.ft.com/stream/7e37c19e-8fa3-439f-a870-b33f0520bcc0'
 
newsHeader ={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    



}


newsResp = rq.get(url=newsUrl,headers=newsHeader)

newssoup =BeautifulSoup(newsResp.content,'html.parser')


All_news = newssoup.find_all('div',attrs={'class':"o-teaser__heading"})

for news in All_news:
    print('news',news.text) 


news_headlines=[news.text for news in All_news]  

news_brief =newssoup.find_all('p',attrs={'class':"o-teaser__standfirst"})
for info in news_brief:

    print('info',info.text)


all_date = newssoup.find_all('time')
for dates in all_date:
    print(dates.attrs['datetime'])

news_data ={
    'Headlines':news_headlines,
    'detail_news':news,
    'news_date': dates

}

newsDf=pd.DataFrame(news_data)
newsDf.to_csv('Fthead.csv')
