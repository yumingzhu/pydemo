#!/root/anaconda3/bin/python
#coding=utf-8
import math
import random

from demo.csdn.sendEmail import senErrorEmail
from retrying import  retry
import  requests
import time
from lxml import etree
import  re
from datetime import datetime
from  fake_useragent import UserAgent
from urllib import request

class Csdn:
    def __init__(self):
        # 递增的url
        self.temp_url="https://edu.csdn.net/course/p{}";
        # 第一次 num
        self.num=1;
        # num 的最大值
        self.max_num=1000
        #是否取获取最大页数
        self.flag=True;
        self.proxy="http://180.121.132.168:3128"
    #失败了 重试三次
    @retry(stop_max_attempt_number=3)
    def getcourse(self,url):
         # ua=UserAgent(verify_ssl=False)
         headers = {
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
             , "Referer": "http://blog.csdn.net"
            , "Connection": "close"}
         response = requests.get(url, headers=headers,timeout=3,proxies=self.proxy)
         html_str=etree.HTML(response.content.decode())
         print(html_str)
         # 存放当前的链接
         list =html_str.xpath("//div[@class='course_item']/a/@href")
         pattern = re.compile(r'\d+')
         if self.flag:
             count_str=html_str.xpath("//span[@class='page-nav']/span[@class='text']/text()")[0]
             count= pattern.findall(count_str)[0] if len(pattern.findall(count_str)) >0  else 0
             self.max_num=math.ceil(int(count)/25+1)
             print(self.max_num)
             self.flag=False
         author_list =[]
         for  href in  list:
             time.sleep(1)
             response_author=requests.get(href, headers=headers,timeout=3)
             author=etree.HTML(response_author.content.decode()).xpath("//a[@class='mr10']/text()")
             if(len(author)>0):
                 student_str = etree.HTML(response_author.content.decode()).xpath("//div[@class='course_status']//span/text()")[0]
                 title=etree.HTML(response_author.content.decode()).xpath("//div[@class='info_right qrcode_box_top']/h1/text()")[0]
                 student_num= pattern.findall(student_str)[0] if len(pattern.findall(student_str)) >0  else 0
                 author_list.append((author[0],title,student_num))
         return  author_list
    def  save_author_list(self,author_list):
        #获取当前时间
        datestr=datetime.now().strftime('%Y-%m-%d')
        # fp=open("/root/yu/csdndata/csdn"+datestr+".txt","a+",encoding='utf-8')
        fp=open("G:/mywork/csdn"+datestr+".txt","a+",encoding='utf-8')
        for  temp in author_list:
            fp.write(temp[0]+"$$")
            fp.write(temp[1]+"$$")
            fp.write(temp[2]+"\n")
        print("完成第%s页的爬取"%self.num)
        self.num=self.num+1


    def  run(self):
        # try:
            while self.num<self.max_num:
                url=self.temp_url.format(self.num)
                author_list=self.getcourse(url)
                self.save_author_list(author_list)
        # except Exception as ex:
        #  senErrorEmail(ex, "您的程序挂了，快来拯救吧！！！")


if __name__ == '__main__':
    csdn=Csdn();
    csdn.run()



