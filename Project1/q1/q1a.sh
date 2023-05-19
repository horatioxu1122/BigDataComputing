/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/output/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -file ./mapper_a.py -mapper ./mapper_a.py -file ./reducer_a.py -reducer ./reducer_a.py -input /q1/input/data.txt -output /q1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /q1/output/*
