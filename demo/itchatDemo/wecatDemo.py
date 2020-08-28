from wxpy import *
bot = Bot()  # 登陆网页微信，并保存登陆状态



    # 搜索自己的好友，注意中文字符前需要+u
my_group = bot.friends().search("mwz")[0]
my_group.send("xxxxxx")  # 发送MSG
