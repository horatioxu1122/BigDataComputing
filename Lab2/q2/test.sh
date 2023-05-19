#!/bin/bash
source ../../env.sh
../../start.sh
hadoop dfsadmin -safemode leave
/usr/local/hadoop/bin/hdfs dfs -rm -r /q2/input/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /q2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../lab2data/data.csv /q2/input/
/usr/local/spark/bin/spark-submit --master=spark://$SPARK_MASTER:7077 ./Part2.py hdfs://$SPARK_MASTER:9000/q2/input/
../../stop.sh

