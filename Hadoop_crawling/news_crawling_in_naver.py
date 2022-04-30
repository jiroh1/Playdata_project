import urllib
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import requests
import time


class Crawl:

    @staticmethod
    def crawling():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        url = 'https://finance.naver.com/news/news_list.nhn?mode=RANK&date=20210718&page=1'
        driver.get(url)
        time.sleep(3)

        # news 기사 및 날짜
        news_sub = driver.find_elements_by_xpath(f'//*[@id="contentarea_left"]/div[2]/ul/li/ul/li/a')
        #date = driver.find_elements_by_xpath(f'//*[@id="contentarea_left"]/div[2]/ul/li/ul/li/span[3]')
        res = list([ele.get_attribute('title') for ele in news_sub])
        print(res)
        #res2 = list([ele.text for ele in date])

        # news=[]
        # f = open('naver_news.txt', 'w', encoding='utf-8')
        # for i in res:
        #     a = i.replace('"'," ").replace("\'","").replace(",","").replace("[","").replace("]","").replace("…","").replace("·"," ")
        #     news.append(a)
        # for j in news:
        #     print(j)
        #     f.write(j+''+'\n')
        # f.close()
        #
if __name__ == '__main__':
    Crawl().crawling()