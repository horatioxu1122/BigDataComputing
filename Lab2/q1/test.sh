#!/bin/bash
source ../../env.sh
../../start.sh
hadoop dfsadmin -safemode leave
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/input/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /q1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../lab2data/shot_logs.csv /q1/input/
/usr/local/spark/bin/spark-submit --master=spark://$SPARK_MASTER:7077 ./Part1.py hdfs://$SPARK_MASTER:9000/q1/input/
../../stop.sh

