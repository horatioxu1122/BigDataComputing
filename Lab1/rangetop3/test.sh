#!/bin/sh
echo "Enter the hour range of interest in the format #-# (example 1-4):"
read input_range
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /rangetop3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /rangetop3/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /rangetop3/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../lab-1/access.log /rangetop3/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../lab-1/rangetop3/mapper1.py -mapper "../../lab-1/rangetop3/mapper1.py $input_range" \
-file ../../lab-1/rangetop3/reducer1.py -reducer ../../lab-1/rangetop3/reducer1.py \
-input /rangetop3/input/* -output /rangetop3/output/


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options=-nr \
-file ../../lab-1/rangetop3/mapper2.py -mapper ../../lab-1/rangetop3/mapper2.py \
-file ../../lab-1/rangetop3/reducer2.py -reducer ../../lab-1/rangetop3/reducer2.py \
-input /rangetop3/output/* -output /rangetop3-2/output/


/usr/local/hadoop/bin/hdfs dfs -cat /rangetop3-2/output/part-00000 | head -3
/usr/local/hadoop/bin/hdfs dfs -rm -r /rangetop3/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /rangetop3/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /rangetop3-2/output/
../../stop.sh
