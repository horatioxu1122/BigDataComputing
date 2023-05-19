#!/bin/sh
base_dir=$(cd "$(dirname "$0")";pwd)
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /grep/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /grep/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /grep/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/test.txt /grep/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/grep/mapper.py -mapper "../../mapreduce-test-python/grep/mapper.py world" \
-file ../../mapreduce-test-python/grep/reducer.py -reducer ../../mapreduce-test-python/grep/reducer.py \
-input /grep/input/* -output /grep/output/
/usr/local/hadoop/bin/hdfs dfs -cat /grep/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /grep/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /grep/output/
../../stop.sh
