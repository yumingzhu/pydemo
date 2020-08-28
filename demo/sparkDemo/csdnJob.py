import datetime
import os
import sys
import time
from datetime import date, timedelta

from pyspark import SparkContext
from pyspark.sql import SparkSession

os.environ['SPARK_HOME'] = 'E:\software\spark-2.1.1-bin-hadoop2.7'
sys.path.append('E:\software\spark-2.1.1-bin-hadoop2.7\python')
propertys={"user":"root","password":"yumingzhu","driver":"com.mysql.jdbc.Driver"}

def createDataFrame(spark, rdd, scheam):
    df = spark.createDataFrame(rdd.map(lambda x: x.split("$$")), schema=schema)
    return df


if __name__ == '__main__':
    starttime = time.time()
    spark = SparkSession.builder.appName("sparkSession").master("local").getOrCreate()
    sc = spark.sparkContext
    yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
    today = date.today().strftime("%Y-%m-%d")
    yesRdd = sc.textFile("G:/mywork/" + "csdn" + yesterday + ".txt");
    toRdd = sc.textFile("G:/mywork/" + "csdn" + today + ".txt");
    # 创建dataframe
    schema = ["name", "title", "number"]
    yesdf = createDataFrame(spark, yesRdd, schema)
    todf = createDataFrame(spark, toRdd, schema)
    yesdf.createOrReplaceTempView("y_view")
    todf.createOrReplaceTempView("t_view")
    dataDf=spark.sql("""
    select  t.name ,t.title,(t.sum-y.sum) as count  from 
                (select  name,title,sum(cast(number  as INT)) as  sum ,count(1) as ct from t_view  group by  name,title) t 
                left  join   (select  name,title,sum(cast(number  as INT)) as  sum ,count(1) as ct  from y_view  group by  name,title) y  where t.name=y.name  and t.title=y.title and concat(t.ct,y.ct) !='21'
    """)
    dataDf.createOrReplaceTempView("data")
    resultDf=spark.sql(
        "select name,sum(count) as sum,current_date as day from  data   where   count>0   group  by  name   order by sum desc");
    resultDf.write.jdbc(url="jdbc:mysql://127.0.0.1:3306/test?useUnicode=true&characterEncoding=UTF-8&zeroDateTimeBehavior=convertToNull&rewriteBatchedStatements=true&tinyInt1isBit=false",table="teacher"
                         ,properties=propertys,mode="overwrite")

    print( dataDf.count())
    #  关闭资源
    sc.stop()
    spark.stop()
    endtime =time.time()
    print(endtime-starttime)
