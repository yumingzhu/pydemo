import os
import sys
import  json
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

os.environ['SPARK_HOME'] = 'E:\software\spark-2.1.1-bin-hadoop2.7'
sys.path.append('E:\software\spark-2.1.1-bin-hadoop2.7\python')
def  getInfo(x):
    try:
        jsonstr=json.loads(x, strict=False)
        city = jsonstr["device"]['geo']['city']
        request_id = jsonstr['request_id']
        return (request_id,city)
    except Exception as ex:
       return None



if __name__ == '__main__':
    sc = SparkContext(appName="PythonWordCount")
    rdd=sc.textFile("G:/test/c.txt")
    rdd.map(getInfo).foreach(lambda  a:print(a))
    # rdd=sc.parallelize(range(1,100000))
    # print(rdd.take(10000))
