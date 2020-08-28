import  os
import sys
from  operator import  add

from pyspark.sql import SparkSession

os.environ['SPARK_HOME'] = 'E:\software\spark-2.1.1-bin-hadoop2.7'
sys.path.append('E:\software\spark-2.1.1-bin-hadoop2.7\python')

if __name__ == '__main__':
    spark=SparkSession.builder.appName("sparkSession").master("local").getOrCreate()
    spark.read.option("header","true").csv("G:/win_notice/*").show()

