import math
from retrying import  retry
import  requests
import time
from lxml import etree
import  re
from datetime import datetime
from fake_useragent import UserAgent
class Csdnlecturer:
    def __init__(self):
        # 递增的url
        self.temp_url="https://edu.csdn.net/lecturer?page={}";
        # 第一次 num
        self.num=1;
        # num 的最大值
        self.max_num=100
        #是否取获取最大页数
        self.flag=True;
    #失败了 重试三次
    # @retry(stop_max_attempt_number=3)
    def getcourse(self,url):
         ua=UserAgent()
         headers = {
            "User-Agent": ua.random
            , "Referer": "http://blog.csdn.net"
            , "Connection": "close"}
         time.sleep(3)
         response = requests.get(url, headers=headers,timeout=3)
         if self.flag:
             sumStr=etree.HTML(response.content.decode()).xpath("//div[@class='panelC clearfix']/span/text()")[0];
             pattern = re.compile(r'\d+')
             count= pattern.findall(sumStr)[0] if len(pattern.findall(sumStr)) >0  else 0
             self.max_num=math.ceil(int(count)/20+1)
             self.flag=False
         hrefs=etree.HTML(response.content.decode()).xpath("//ul[@class='list-inline clearfix']/li/a/@href")
         names=etree.HTML(response.content.decode()).xpath("//ul[@class='list-inline clearfix']/li/a/text()")
         list_name=[]
         return  names,hrefs
    def  save_author_list(self,names,hrefs):
        #获取当前时间
        fp=open("/root/yu/csdndata/lecturer.txt","a+",encoding='utf-8')
        # fp=open("G:/mywork/csdn"+datestr+".txt","a+",encoding='utf-8')
        for  temp in range(len(names)):
            fp.write(names[temp]+"$$"+hrefs[temp].split("/")[4])
            fp.write("\n")



    def  run(self):
            # try:
                while self.num<self.max_num:
                    url=self.temp_url.format(self.num)
                    names,hrefs=self.getcourse(url)
                    self.save_author_list(names,hrefs)
                    print("完成第%s页的爬取"%self.num)
                    self.num=self.num+1
            # except Exception as ex:
            #  senErrorEmail(ex, "您的程序挂了，快来拯救吧！！！")


if __name__ == '__main__':
    csdn=Csdnlecturer();
    csdn.run()



