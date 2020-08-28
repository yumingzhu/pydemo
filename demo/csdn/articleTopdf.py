import os
import pdfkit
import datetime
import wechatsogou
# 初始化API

ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)
def url2pdf(url, title, targetPath):
    '''
    使用pdfkit生成pdf文件
    :param url: 文章url
    :param title: 文章标题
    :param targetPath: 存储pdf文件的路径
    '''
    try:
        content_info = ws_api.get_article_content(url)
    except:
        return False
    # 处理后的html
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
    </head>
    <body>
    <h2 style="text-align: center;font-weight: 400;">{title}</h2>
    {content_info['content_html']}
    </body>
    </html>
    '''
    try:
        path_wk="E:/softwareAPP/wkhtmltopdf/bin/wkhtmltopdf.exe";
        config=pdfkit.configuration(wkhtmltopdf=path_wk)
        pdfkit.from_string(input=html, output_path=targetPath,configuration=config)

    except:
        # 部分文章标题含特殊字符，不能作为文件名
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.pdf'
        pdfkit.from_string(html, targetPath + os.path.sep + filename)



if __name__ == '__main__':
    # 此处为要爬取公众号的名称

    url2pdf("https://mp.weixin.qq.com/s/wwT5n2JwEEAkrrmOhedziw", "HBase的系统架构全视角解读","G:/test/hbase文档.pdf" )
    # gzh_name = ''
    # # 如果不存在目标文件夹就进行创建
    # if not os.path.exists(targetPath):
    #     os.makedirs(targetPath)
    # # 将该公众号最近10篇文章信息以字典形式返回
    # data = ws_api.get_gzh_article_by_history(gzh_name)
    # article_list = data['article']
    # for article in article_list:
    #     url = article['content_url']
    #     title = article['title']
    #     url2pdf(url, title, targetPath)