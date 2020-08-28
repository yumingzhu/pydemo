import math
from demo.csdn.sendEmail import senErrorEmail
from retrying import retry
import requests
import time
from lxml import etree
import re
from datetime import datetime
from fake_useragent import UserAgent


class Csdn:
    def __init__(self):
        # 递增的url
        self.temp_url = "https://edu.csdn.net/course/p{}";
        # 第一次 num
        self.num = 1;
        # num 的最大值
        self.max_num = 1000
        # 是否取获取最大页数
        self.flag = True;

    # 失败了 重试三次
    @retry(stop_max_attempt_number=3)
    def getcourse(self, url):
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random
            , "Referer": "http://blog.csdn.net"
            , "Connection": "close"}
        response = requests.get(url, headers=headers, timeout=3)
        html_str = etree.HTML(response.content.decode())
        # 存放当前的链接
        list = html_str.xpath("//div[@class='course_item']/a/@href")
        pattern = re.compile(r'\d+')
        if self.flag:
            count_str = html_str.xpath("//span[@class='page-nav']/span[@class='text']/text()")[0]
            count = pattern.findall(count_str)[0] if len(pattern.findall(count_str)) > 0 else 0
            self.max_num = math.ceil(int(count) / 25 + 1)
            self.flag = False
        author_list = []
        for href in list:
            time.sleep(2)
            response_author = requests.get(href, headers=headers, timeout=3)
            author = etree.HTML(response_author.content.decode()).xpath("//a[@class='mr10']/text()")

            if (len(author) > 0):
                idstr = etree.HTML(response_author.content.decode()).xpath("//a[@class='mr10']/@href")[0]
                id = pattern.findall(idstr)[0] if len(pattern.findall(idstr)) > 0 else 0
                student_str = \
                    etree.HTML(response_author.content.decode()).xpath("//div[@class='course_status']//span/text()")[0]
                title = etree.HTML(response_author.content.decode()).xpath(
                    "//div[@class='info_right qrcode_box_top']/h1/text()")[0]
                student_num = pattern.findall(student_str)[0] if len(pattern.findall(student_str)) > 0 else 0
                author_list.append((author[0], id, title, student_num))
        return author_list

    def save_author_list(self, author_list):
        # 获取当前时间
        datestr = datetime.now().strftime('%Y-%m-%d')
        # fp=open("/root/yu/csdndata/csdn-"+datestr+".txt","a+",encoding='utf-8')
        fp = open("G:/mywork/csdn" + datestr + ".txt", "a+", encoding='utf-8')
        for temp in author_list:
            fp.write(temp[0] + "$$")
            fp.write(temp[1] + "$$")
            fp.write(temp[2] + "$$")
            fp.write(temp[3] + "\n")
        print("完成第%s页的爬取" % self.num)
        self.num = self.num + 1

    def run(self):
        while self.num < self.max_num:
            url = self.temp_url.format(self.num)
            author_list = self.getcourse(url)
            self.save_author_list(author_list)


if __name__ == '__main__':
    csdn = Csdn();
    csdn.run()
