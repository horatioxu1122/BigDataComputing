from __future__ import print_function
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: prob <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("Ticket")\
        .getOrCreate()

    df = spark.read.csv(sys.argv[1], header=True, inferSchema=True)
    df_dropna_1 = df.where(col("Street Code1").isNotNull())
    df_dropna_2 = df_dropna_1.where(col("Street Code2").isNotNull())
    df_dropna_3 = df_dropna_2.where(col("Street Code3").isNotNull())
    df_dropna_final = df_dropna_3.where(col("Vehicle Color").isNotNull())
    assembler = VectorAssembler(inputCols=['Street Code1', 'Street Code2', 'Street Code3'], outputCol='features')
    new_df = assembler.transform(df_dropna_final)
    kmeans = KMeans(k=3, maxIter=1, seed=1)
    model = kmeans.fit(new_df.select("features"))
    predictions = model.transform(new_df).select("Street Code1", "Street Code2", "Street Code3", "features", "Vehicle Color", "prediction")
    clustered_df = predictions.withColumnRenamed("prediction", "cluster")
    street = [34510,10030,34050]
    street_df=clustered_df.filter((clustered_df['Street Code1'].isin(street))|(clustered_df['Street Code2'].isin(street))|(clustered_df['Street Code3'].isin(street)))
    black_colors=["Black", "BLK", "BK", "BK.", "BLAC", "BK/","BCK","BLK.","B LAC","BC"]
    black_street_df = street_df.withColumn("isBlack", when(col("Vehicle Color").isin(black_colors), "Black").otherwise("NotBlack"))
    result = black_street_df.groupBy('cluster').agg(sum((black_street_df.isBlack == 'Black').cast('int')).alias('num_black'),count('*').alias('num_vehicle')).withColumn('probability', col('num_black') / col('num_vehicle'))
    result.show()

    spark.stop()

