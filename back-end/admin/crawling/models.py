import csv
import datetime as dt
import nltk
import pandas as pd
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from admin.common.models import ValueObject
from selenium import webdriver
from nltk.tokenize import word_tokenize


class Crawling(object):
    def __init__(self):
        pass

    def process(self):
        nltk.download()
        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        # self.samsung_report(vo)

    def samsung_report(self, vo):
        okt = Okt()
        okt.pos('삼성전자 글로벌센터 전자사업부', stem=True)
        with open('admin/crawling/data/kr-Report_2018.txt', 'r', encoding='UTF-8') as f:
            texts = f.read()
        print(texts)

    def naver_movie(self):
        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        vo.url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        driver = webdriver.Chrome(f'{vo.context}/chromedriver')
        driver.get(vo.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class': 'tit3'})
        movie_name = [div.a.string for div in all_div]
        for i in movie_name:
            print(i)
        dt = {i: movie_name[i] for i in range(len(movie_name))}
        # dt = {i + 1: val for i, val in enumerate(movie_name)}
        with open(vo.context + 'naver_movie.csv', 'w', encoding='UTF-8') as f:
            w = csv.writer(f)
            w.writerow(dt.keys())
            w.writerow(dt.values())
        driver.close()

    def tweet_trump(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwiches', ['enable-logging'])
        driver = webdriver.Chrome('/admin/crawling/data/chromedriver', options=options)

        start_date = dt.date(year=2018, month=12, day=1)
        until_date = dt.date(year=2018, month=12, day=2)
        end_date = dt.date(year=2018, month=12, day=2)
        query = 'Donald Trump'
        total_tweets = []
        url = f'https://twitter.com/search?q={query}%20' \
              f'since%3A{str(start_date)}%20until%3A{str(until_date)}&amp;amp;amp;amp;amp;amp;lang=eg'
        while not end_date == start_date:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            last_height = driver.execute_script('return document.body.scrollHeight')
            while True:
                daily_freq = {'Date': start_date}
                word_freq = 0
                tweets = soup.find_all('p', {'class': 'TweetTextSize'})
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                new_height = driver.execute_script('return document.body.scrollHeight')
                if new_height != last_height:
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    tweets = soup.find_all('p', {'class', 'TweetTextSize'})
                    word_freq = len(tweets)
                else:
                    daily_freq['Frequency'] == word_freq
                    word_freq = 0
                    start_date = until_date
                    until_date = dt.timedelta(days=1)
                    daily_freq = {}
                    total_tweets.append(tweets)
                    all_div = soup.find_all('div', {'class', 'css-901oao'})
                    arr = [span.string for span in all_div]
                    for i in arr:
                        print(i)
                    break
                last_height = new_height

        '''trump_df = pd.DataFrame(columns=['id', 'message'])
        number = 1
        for i in range(len(total_tweets)):
            for j in range(len(total_tweets[i])):
                trump_df = trump_df.append({'id':number, 'message': (total_tweets[i][j]).text},
                                           ignore_index=True)
                number = number + 1
        print(trump_df.head())'''
