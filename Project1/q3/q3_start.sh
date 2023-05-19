#!/bin/sh
../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /q3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q3/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p  /q3/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../q1/data.txt /q3/input
echo "Copy and startup complete"
