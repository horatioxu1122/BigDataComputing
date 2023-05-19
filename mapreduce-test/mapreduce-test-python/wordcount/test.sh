#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /wordcount/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/test.txt /wordcount/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/wordcount/mapper.py -mapper ../../mapreduce-test-python/wordcount/mapper.py \
-file ../../mapreduce-test-python/wordcount/reducer.py -reducer ../../mapreduce-test-python/wordcount/reducer.py \
-input /wordcount/input/* -output /wordcount/output/
/usr/local/hadoop/bin/hdfs dfs -cat /wordcount/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount/output/
../../stop.sh
