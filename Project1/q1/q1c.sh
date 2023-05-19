/usr/local/hadoop/bin/hdfs dfs -rm -r /q1/output/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -file ./mapper_c.py -mapper ./mapper_c.py -file ./reducer_c.py -reducer ./reducer_c.py -input /q1/input/data.txt -output /q1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /q1/output/*
