from __future__ import print_function
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import month
from pyspark.sql.functions import count
from pyspark.sql.functions import to_date
from pyspark.sql.functions import col


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sort <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("DateCount")\
        .config("spark.default.parallelism", "2") \
        .getOrCreate()

    df = spark.read.csv(sys.argv[1], header=True, inferSchema=True)

    df_new = df.select(col("Issue Date"),to_date(col("Issue Date"),"MM/dd/yyyy").alias("date"))

    df_new_new = df_new.withColumn('month', month('date'))

    # Count number of occurrences of each month
    df_month_count = df_new_new.groupBy('month').agg(count('*').alias('count'))

    # Find month with highest frequency
    df_month_count.orderBy(df_month_count['count'].desc()).show(1)

    # Stop the SparkSession
    spark.stop()
