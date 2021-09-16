#!/bin/bash
PYSPARK_PYTHON=python spark-submit \
    --conf spark.streaming.batch.duration=5 --conf spark.ui.port=4041\
    --master local[*] \
    LogStream.py "$1" "$2"
#args:
#argv[1], "/tmp/checkpoint-write", checkpoint location
#argv[2], "/var/log/my_server/instance5.log.*", path to the input directory
