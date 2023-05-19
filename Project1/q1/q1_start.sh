#!/bin/sh
../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p  /q1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ./data.txt /q1/input
echo "Copy and startup complete"
