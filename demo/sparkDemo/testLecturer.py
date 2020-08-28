import datetime
import os
import sys
import time
from operator import add

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

os.environ['SPARK_HOME'] = 'E:\software\spark-2.1.1-bin-hadoop2.7'
sys.path.append('E:\software\spark-2.1.1-bin-hadoop2.7\python')
propertys={"user":"root","password":"yumingzhu","driver":"com.mysql.jdbc.Driver"}

def  filterFun(a):
    if a[1]>1:
        return True

if __name__ == '__main__':
    starttime = time.time()
    conf=SparkConf()
    conf.set("spark.some.config.option", "some-value")
    conf.set("spark.jars","E:\software\spark-2.1.1-bin-hadoop2.7\mysql-connector-java-5.1.30.jar")

    spark = SparkSession.builder.appName("sparkSession").config("spark.jars","E:\software\spark-2.1.1-bin-hadoop2.7\mysql-connector-java-5.1.30.jar").master("local").getOrCreate()

    df=spark.read.jdbc(url="jdbc:mysql://127.0.0.1:3306/test?useUnicode=true&characterEncoding=UTF-8&zeroDateTimeBehavior=convertToNull&rewriteBatchedStatements=true&tinyInt1isBit=false",table="teacher"
                         ,properties=propertys)
    df.show()
    # sc.textFile("G:/mywork/lecturer.txt").map(lambda x:(x.split("$$")[0],1)).reduceByKey(add).filter(filterFun).foreach(lambda  a:print(a))
