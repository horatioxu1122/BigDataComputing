package hadoop.mapreduce.test.grep;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

/**
 * Hello world!
 *
 */
public class RunJob
{
    public static void main(String[] args) {
        if(args.length < 1){
            System.out.println("Pattern not found!");
            return;
        }
        Configuration config = new Configuration();
        try {
            FileSystem fs = FileSystem.get(config);
            //获取参数
            String pattern = args[0];
            config.set("grep", pattern);
            Job job = Job.getInstance(config);
            job.setJobName("Grep");
            job.setJarByClass(RunJob.class);
            job.setMapperClass(GrepMapper.class);
            job.setReducerClass(GrepReducer.class);
            job.setMapOutputKeyClass(Text.class);
            job.setMapOutputValueClass(IntWritable.class);
            //设置输入目录
            FileInputFormat.addInputPath(job, new Path("/grep/input/"));
            //设置输出目录
            Path outPath = new Path("/grep/output");
            if(fs.exists(outPath)){
                fs.delete(outPath, true);
            }
            FileOutputFormat.setOutputPath(job, outPath);
            Boolean result = job.waitForCompletion(true);
            if(result){
                System.out.println("Job is complete!");
            }else{
                System.out.println("Job is fail!");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
