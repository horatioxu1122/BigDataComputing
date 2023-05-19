#!/bin/sh
../../start.sh
mvn clean package
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /logstat/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/access.log /logstat/input/
/usr/local/hadoop/bin/hadoop jar target/mapreduce-test-logstat-1.0-SNAPSHOT.jar hadoop.mapreduce.test.logstat.RunJob
/usr/local/hadoop/bin/hdfs dfs -cat /logstat/output/part-r-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat/output/
mvn clean
../../stop.sh
