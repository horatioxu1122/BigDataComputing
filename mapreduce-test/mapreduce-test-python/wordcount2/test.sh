#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /wordcount2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/test.txt /wordcount2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/wordcount2/mapper.py -mapper ../../mapreduce-test-python/wordcount2/mapper.py \
-file ../../mapreduce-test-python/wordcount2/reducer.py -reducer ../../mapreduce-test-python/wordcount2/reducer.py \
-input /wordcount2/input/* -output /wordcount2/output/
/usr/local/hadoop/bin/hdfs dfs -cat /wordcount2/output/part-00000 | tail -100
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount2/output/
../../stop.sh
