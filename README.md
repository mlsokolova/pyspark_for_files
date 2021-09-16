Create miniconda3 enviroment:  
```conda create -n pyspark python=3.9 pip wheel pandas pyspark ipykernel```  

Run:  
```submit.sh  <checkpoint location> <input path>```  

refs:  
https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/DataStreamReader.html  
https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#input-sources  
