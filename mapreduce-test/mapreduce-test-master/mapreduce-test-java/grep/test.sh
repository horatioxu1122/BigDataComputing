#!/bin/sh
../../start.sh
mvn clean package
/usr/local/hadoop/bin/hdfs dfs -rm -r /grep/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /grep/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /grep/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/test.txt /grep/input/
/usr/local/hadoop/bin/hadoop jar target/mapreduce-test-grep-1.0-SNAPSHOT.jar hadoop.mapreduce.test.grep.RunJob world
/usr/local/hadoop/bin/hdfs dfs -cat /grep/output/part-r-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /grep/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /grep/output/
mvn clean
../../stop.sh
