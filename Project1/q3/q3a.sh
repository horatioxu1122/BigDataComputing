clustrs=5
/usr/local/hadoop/bin/hdfs dfs -rm -r /q3/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /q3/output_points/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -file ./mapper_a1.py -mapper ./mapper_a1.py -file ./reducer_a1.py -reducer ./reducer_a1.py -input /q1/input/data.txt -output /q3/output_points/ -numReduceTasks $clustrs
for a in {1..10}
do
x="$(hdfs dfs -cat /q3/output_points/*)"
/usr/local/hadoop/bin/hdfs dfs -rm -r /q3/output_points/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -file ./mapper_a2.py -mapper "./mapper_a2.py $x"  -file ./reducer_a2.py -reducer ./reducer_a2.py -input /q1/input/data.txt -output /q3/output_points/
done
/usr/local/hadoop/bin/hdfs dfs -cat /q3/output_points/*
