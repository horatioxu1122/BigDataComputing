package hadoop.mapreduce.test.wordcount2;

import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;


public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    protected void map(LongWritable key, Text value,Context context)
            throws IOException, InterruptedException {
        String[] words = StringUtils.split(value.toString(), ' ');
        for(int i=0;i<words.length;i++){
            if(i > 0){
                String word = words[i-1] + " " + words[i];
                context.write(new Text(word), new IntWritable(1));
            }
        }
    }
}