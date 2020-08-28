
import pdfkit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    , "Referer": "http://blog.csdn.net"
    , "Connection": "close"
    , 'content-type': 'application/json;charset=utf-8'
}

path_wk = "E:/softwareAPP/wkhtmltopdf/bin/wkhtmltopdf.exe";
config = pdfkit.configuration(wkhtmltopdf=path_wk)
pdfkit.from_url("https://blog.csdn.net/weixin_30267691/article/details/98638295","G:/test/xx.pdf",configuration=config)