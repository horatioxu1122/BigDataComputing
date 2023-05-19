#!/bin/sh
../../start.sh
mvn clean package
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /wordcount2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/test.txt /wordcount2/input/
/usr/local/hadoop/bin/hadoop jar target/mapreduce-test-wordcount2-1.0-SNAPSHOT.jar hadoop.mapreduce.test.wordcount2.RunJob
/usr/local/hadoop/bin/hdfs dfs -cat /wordcount2/output/part-r-00000 | tail -100
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /wordcount2/output/
mvn clean
../../stop.sh
