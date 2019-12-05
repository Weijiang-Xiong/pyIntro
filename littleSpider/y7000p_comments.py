
import requests
import json
import os
import time
import random
import jieba
from wordcloud import WordCloud
from imageio import imread

comment_file_path = 'jd_comments.txt'

def get_spider_comments(page = 0):

    #爬取某东评论
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1748&productId=100004014613&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%page
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'referer':'https://item.jd.com/100004014613.html'

    }
    # url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv7990&productId=1070129528&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&rid=0&fold=1'%page
    # headers = {

    #     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    #     'referer':'https://item.jd.com/1070129528.html'
    # }
    try:
        response = requests.get(url, headers = headers)
    except:
        print("something wrong!")
    #获取json格式数据集
    comments_json = response.text[26:-2]
    #将json数据集转为json对象
    comments_json_obj = json.loads(comments_json)
    #获取comments里面的所有内容
    comments_all = comments_json_obj['comments']
    #获取comments中评论content的内容
    for comment in comments_all:
        with open(comment_file_path,'a+' ,encoding='utf-8') as fin:
            fin.write(comment['content']+'\n')
        print(comment['content'])

def batch_spider_comments():
    # 每次写入数据之前先清空文件
    if os.path.exists(comment_file_path):
        os.remove(comment_file_path)
    for i in range(1,100):
        print('正在爬取'+str(i+1)+'页数据。。。。')
        get_spider_comments(i)
        time.sleep(random.random()*5)

def cut_word():
    with open(comment_file_path, 'r', encoding='utf-8') as file:
        comment_text = file.read()
        wordlist = jieba.lcut_for_search(comment_text)
        new_wordlist = ' '.join(wordlist)
        return new_wordlist

def create_word_cloud():
    mask = imread('/littleSpider/ball.jpg')
    wordcloud = WordCloud(font_path='msyh.ttc',mask = mask).generate(cut_word())
    wordcloud.to_file('/littleSpider/picture.png')

if __name__ == '__main__':
    if os.path.exists(comment_file_path):
        create_word_cloud()
    else:
        batch_spider_comments()
        create_word_cloud()
    