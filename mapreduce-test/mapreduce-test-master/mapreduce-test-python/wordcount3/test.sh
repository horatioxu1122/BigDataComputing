#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount3/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /wordcount3/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/test.txt /wordcount3/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/wordcount3/mapper-1.py -mapper ../../mapreduce-test-python/wordcount3/mapper-1.py \
-file ../../mapreduce-test-python/wordcount3/reducer-1.py -reducer ../../mapreduce-test-python/wordcount3/reducer-1.py \
-input /wordcount3/input/* -output /wordcount3/output/


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/wordcount3/mapper-2.py -mapper ../../mapreduce-test-python/wordcount3/mapper-2.py \
-file ../../mapreduce-test-python/wordcount3/reducer-2.py -reducer ../../mapreduce-test-python/wordcount3/reducer-2.py \
-input /wordcount3/output/* -output /wordcount3-2/output/





/usr/local/hadoop/bin/hdfs dfs -cat /wordcount3-2/output/part-00000 | tail -10
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount3/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount3-2/output/
../../stop.sh
