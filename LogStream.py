# -*- coding: utf-8 -*-
#!/home/masha/miniconda3/envs/pyspark/bin/python

from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
import sys

spark = SparkSession.builder.appName("LogProcessor").getOrCreate()
spark.sparkContext.setLogLevel('WARN')

checkpointlocation=sys.argv[1]
logs_path=sys.argv[2]
#print(logs_path)

## Считываем 
st = spark \
  .readStream \
  .format("text") \
  .option("path",logs_path)\
  .option("maxFilesPerTrigger",1)\
  .load() 

## Выводим в консоль

query = st\
    .writeStream \
    .format("console") \
    .option("checkpointLocation", checkpointlocation)\
    .option("numRows",10000)\
    .option("truncate",False)\
    .start()\

query.awaitTermination()
