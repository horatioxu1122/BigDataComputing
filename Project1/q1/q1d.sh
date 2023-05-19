/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/output/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ./mapper_d.py -mapper ./mapper_d.py -file \
./reducer_d.py -reducer ./reducer_d.py -input /q1/input/data.txt -output /q1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /q1/output/*
