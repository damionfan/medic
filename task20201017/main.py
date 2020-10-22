# encoding: utf-8
# Author    : damionfan@163.com
# Datetime  : 2020/2/15 20:50
# User      : Damion Fan
# Product   : PyCharm
# Project   : arxiv
# File      : NewPaper.py
# explain   : 参考代码地 http://gwang-cv.github.io/2016/04/01/Python%E7%88%AC%E5%8F%96arxiv%E7%9A%84paper/

from urllib import request

import http.client
import hashlib
import urllib
import random
import json

from bs4 import BeautifulSoup
import re

from ouremail import Satrt_email


def getHtml(url):
    content = request.urlopen(url).read()
    return content.decode('utf-8')


def getContent(content):
    soup = BeautifulSoup(content, 'lxml')
    urls = soup.find_all(name='span', attrs={'class': 'list-identifier'})
    links = []
    for url in urls:
        link = url.find_all(name='a', href=True)
        links.append(link[0]['href'])

    return links


def getInformation(base_url, href):
    content = getHtml(base_url + href)
    soup = BeautifulSoup(content, 'lxml')
    title = soup.find_all(name='h1', attrs={'class': 'title mathjax'})
    title = title[0].get_text().split('\n')[1]

    authors = soup.find_all(name='div', attrs={'class': 'authors'})
    authors = authors[0].get_text().split('\n')
    string = ""
    for author in range(1, len(authors)):
        string += authors[author]
    authors = string

    abstract = soup.find_all(name='blockquote', attrs={'class': 'abstract mathjax'})
    abstract = abstract[0].get_text().replace('\n', ' ')

    # print(abstract)
    # print(translation(abstract))

    meta = soup.find_all(name='td', attrs={'class': 'tablecell comments'})
    comment = ''
    if len(meta) > 0:
        comment = meta[0].get_text()

    # print(title,authors,abstract,comment,zh_title,zh_abstract)
    return title, authors, abstract, comment


def getTotal(url):
    # url = 'http://xxx.itp.ac.cn/list/cs.LG/pastweek'
    # u = 'http://xxx.itp.ac.cn/list/cs.LG/pastweek?show=618'
    # print(url)
    content = getHtml(url)
    soup = BeautifulSoup(content, 'lxml')
    h3 = soup.find_all(name='small')
    # print(h3)
    # print(h3[0].get_text())

    all = h3[0].get_text()
    print(all)
    total = all.split(' ')
    if len(total) < 9:
        total = 100
    else:
        total = total[8]
    # print(total)
    return total


import time


def process_html(base_url, flag):
    total = getTotal(base_url + '/list/' + flag + '/pastweek')
    print(total)
    page = getHtml(base_url + '/list/' + flag + '/pastweek?show=' + total)
    links = getContent(page)
    subject = str(time.strftime("%Y-%m-%d", time.localtime())) + '###'+str(flag)
    string = ''
    num = 0
    for link in links:
        num += 1
        title, authors, abstract, comment = getInformation(base_url, link)
        string += '【' + str(num) + '】' + '\t' + title+'\n'
        string += 'Authors:\t' + authors + '\n'
        string += 'Abstract:\t' + abstract + '\n'
        string += 'Comment:\t' + comment + '\n'
        arxiv_id = re.sub(r'(/)|([a-zA-Z])', '', link)
        download_url = base_url + '/pdf/' + arxiv_id
        # print(arxiv_id)
        string += 'Download:\t' + download_url + '\n\n'
    Satrt_email(subject, string)


if __name__ == '__main__':
    base_url = 'http://xxx.itp.ac.cn/'

    keyword = ['cs.dc', 'cs.ar', 'cs.ni']
    DATA = str(time.strftime("%Y-%m-%d", time.localtime()))
    while True:
        if DATA != str(time.strftime("%Y-%m-%d", time.localtime())):
            DATA = str(time.strftime("%Y-%m-%d", time.localtime()))
            for key in keyword:
                process_html(base_url, key)

'''
待完善功能:
1、自动发微博功能 finished
2、判断是否投顶会
3、关键词判断
4、邮件功能 finished 
5、微信小程序功能
6、整合微博和邮件功能
7、存储文件到本地，然后根据本地信息进行发送邮件等功能
'''
