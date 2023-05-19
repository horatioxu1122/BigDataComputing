#!/bin/sh
../../start.sh
mvn clean package
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /logstat2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/access.log /logstat2/input/
/usr/local/hadoop/bin/hadoop jar target/mapreduce-test-logstat2-1.0-SNAPSHOT.jar hadoop.mapreduce.test.logstat2.RunJob
/usr/local/hadoop/bin/hdfs dfs -cat /logstat2/output/part-r-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/output/
mvn clean
../../stop.sh
