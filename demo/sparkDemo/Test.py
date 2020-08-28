from  datetime import  datetime,date,timedelta

yesterday=(date.today() + timedelta(days = -1)).strftime("%Y-%m-%d")  # 昨天日期
print(yesterday)
