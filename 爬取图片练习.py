#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 爬取图片练习.py
# @Author: JinQiu
# @Date  : 2020/11/27
from lxml import  etree
import requests


heards = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
for i in range(100,170):
    url = 'http://pic.netbian.com/4kmeinv/index_{}.html'.format(i)
    print(url)

    res = requests.get(url=url,headers=heards).text
    tree = etree.HTML(res)
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    for li in li_list:
        img_html = 'http://pic.netbian.com/'+li.xpath('./a/@href')[0]
        print(img_html)
        # for html_url in img_html:
        res1 = requests.get(url=img_html,headers=heards).text
        tree1 = etree.HTML(res1)
        img = tree1.xpath('//*[@id="img"]/img/@src')[0]



        new_url =  'http://pic.netbian.com/'+img
        imgs = requests.get(url=new_url,headers=heards).content
        img_name = img.split('/')[-1] +".jpg"
        img_path = './img_4K/'+img_name
        with open(img_path,'wb') as f:
            f.write(imgs)
            print(img_name, '下载完成')

