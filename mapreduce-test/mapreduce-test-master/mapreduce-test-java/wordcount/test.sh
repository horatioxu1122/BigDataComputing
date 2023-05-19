#!/bin/sh
../../start.sh
mvn clean package
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /wordcount/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/test.txt /wordcount/input/
/usr/local/hadoop/bin/hadoop jar target/mapreduce-test-wordcount-1.0-SNAPSHOT.jar hadoop.mapreduce.test.wordcount.RunJob
/usr/local/hadoop/bin/hdfs dfs -cat /wordcount/output/part-r-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount/output/
mvn clean
../../stop.sh
