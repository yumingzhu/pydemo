import os
import sys

import fn as fn
from pyspark import SparkConf, SparkContext
from pyspark.sql import Row, SparkSession, Window
from pyspark.sql.functions import to_date, to_timestamp,date_format

os.environ['SPARK_HOME'] = 'E:\software\spark-2.1.1-bin-hadoop2.7'
sys.path.append('E:\software\spark-2.1.1-bin-hadoop2.7\python')

def CreateSparkContex():
    sparkconf = SparkConf().setAppName("MYPRO").set("spark.ui.showConsoleProgress", "false")
    sc = SparkContext(conf=sparkconf)
    print("master:" + sc.master)
    sc.setLogLevel("WARN")
    #os.Setpath(sc)
    spark = SparkSession.builder.config(conf=sparkconf).getOrCreate()
    return sc, spark

sc, spark = CreateSparkContex()

parents = os.listdir(u'/apps/eagle-file/t-log')
path=u'/apps/eagle-file/t-log'

from datetime import datetime, date, timedelta
import datetime

# 设置运行的参数：时间、媒体、媒体对应点位
lastday=datetime.date(2019,4,14)
startday=datetime.date(2019,4,14)

excute_list=[]
for i in range((lastday-startday).days + 1):
    excute_day=startday + timedelta(days = i)
    excute_list.append(str(excute_day)+'.log')

list_path=[]
parents.sort()
for parent in parents:
    if parent in excute_list:
        child = os.path.join(path,parent)
        list_path.append(child)

# 将列表中的元素合并成一个文本，以逗号分隔，因为textFile能读取这样的多个文件
list_path_2 = ",".join(list_path)

textDF = sc.textFile(list_path_2)
textDF_1=textDF.map(lambda x:x.split(","))
df=textDF_1.toDF()

df.show();


#
df1=df.withColumn("date_time",to_timestamp('_2', 'yyyy-MM-dd HH:mm:ss:SSSSSS'))
df1.withColumn("row_number", fn.row_number().over(Window.partitionBy("_5").orderBy(df1["date_time"].desc()))).take(1)