package hadoop.mapreduce.test.grep;

import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;

import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class GrepMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    protected void map(LongWritable key, Text value,Context context)
            throws IOException, InterruptedException {
        //get grep pattern
        String pattern = context.getConfiguration().get("grep");
        String str = value.toString();
        //split every line
        String[] lines = str.split("\n");
        for(String line : lines){
            //check if match the pattern
            Pattern r = Pattern.compile(pattern);
            Matcher m = r.matcher(line);
            if (m.find()) {
                //add to input
                context.write(new Text("input"), new IntWritable(1));
            }
        }
    }
}
