package hadoop.mapreduce.test.grep;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class GrepReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    protected void reduce(Text arg0, Iterable<IntWritable> arg1,Context arg2)
            throws IOException, InterruptedException {
        int sum = 0;
        for(IntWritable i : arg1){
            sum += i.get();
        }
        arg2.write(arg0, new IntWritable(sum));
    }

}