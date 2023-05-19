#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /hourlytop3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /hourlytop3/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /hourlytop3/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../lab-1/access.log /hourlytop3/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../lab-1/hourlytop3/mapper1.py -mapper ../../lab-1/hourlytop3/mapper1.py \
-file ../../lab-1/hourlytop3/reducer1.py -reducer ../../lab-1/hourlytop3/reducer1.py \
-input /hourlytop3/input/* -output /hourlytop3/output/


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../lab-1/hourlytop3/mapper2.py -mapper ../../lab-1/hourlytop3/mapper2.py \
-file ../../lab-1/hourlytop3/reducer2.py -reducer ../../lab-1/hourlytop3/reducer2.py \
-input /hourlytop3/output/* -output /hourlytop3-2/output/


/usr/local/hadoop/bin/hdfs dfs -cat /hourlytop3-2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /hourlytop3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /hourlytop3/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /hourlytop3-2/output/
../../stop.sh
