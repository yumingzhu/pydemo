import os
import sys
from operator import add



from pyspark import SparkContext
from pyspark.sql import SparkSession

os.environ['SPARK_HOME'] = 'E:\software\spark-2.1.1-bin-hadoop2.7'
sys.path.append('E:\software\spark-2.1.1-bin-hadoop2.7\python')

if __name__ == '__main__':
    sc = SparkContext(appName="PythonWordCount")
    sc
    lines = sc.textFile('G:/test/ham.txt')
    counts = lines.flatMap(lambda x: x.split(' ')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))
    sc.stop()