#!/bin/bash
source ../../env.sh
../../start.sh
hadoop dfsadmin -safemode leave
/usr/local/hadoop/bin/hdfs dfs -rm -r /P2/Part2/input/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /P2/Part2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal framingham.csv /P2/Part2/input/
/usr/local/spark/bin/spark-submit --master=spark://$SPARK_MASTER:7077 ./proj2.py hdfs://$SPARK_MASTER:9000/P2/Part2/input/
../../stop.sh
