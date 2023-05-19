from __future__ import print_function
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: cluster <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("ComfortableZones")\
        .getOrCreate()

    df = spark.read.csv(sys.argv[1], header=True, inferSchema=True)
    df_dropna = df.where(col("SHOT_CLOCK").isNotNull())
    assembler = VectorAssembler(inputCols=['SHOT_CLOCK', 'SHOT_DIST', 'CLOSE_DEF_DIST'], outputCol='features')
    new_df = assembler.transform(df_dropna)

    grouped_df = new_df.groupBy('player_name').agg(collect_list('features').alias('features'))

    k = 4
    max_iter = 1
    results = []
    for row in grouped_df.collect():
        player = row['player_name']
        features = row['features']
        data = spark.createDataFrame([(v,) for v in features], ['features'])
        kmeans = KMeans(k=k, maxIter=max_iter, seed=1)
        model = kmeans.fit(data)
        predictions = model.transform(data)
        results += [(player, v[0], int(v[1])) for v in predictions.collect()]

    output_df = spark.createDataFrame(results, ['player_name', 'features', 'cluster'])
    new_output_df = new_df.join(output_df, (new_df.player_name == output_df.player_name) & (new_df.features == output_df.features)).drop(output_df.player_name).drop(output_df.features)
    dictionary = {0:'Zone 1', 1:'Zone 2', 2:'Zone 3', 3:'Zone 4'}
    mapping_expr = create_map([lit(x) for x in chain(*dictionary.items())])
    new_df_1 = new_output_df.withColumn("Zone",mapping_expr[col("cluster")])

    James_Harden = new_df_1.where(new_df_1.player_name=='james harden').select(col("player_name"),col("Zone"),col("SHOT_RESULT"))
    Harden_result = James_Harden.groupBy('Zone').agg(sum((James_Harden.SHOT_RESULT == 'made').cast('int')).alias('num_made'),count('*').alias('num_shot')).withColumn('hit_rate', col('num_made') / col('num_shot'))
    Harden_max_hit_rate = Harden_result.select('Zone', 'hit_rate').orderBy(desc('hit_rate')).first()
    print(f"James Harden: {Harden_max_hit_rate[0]}, hit rate: {Harden_max_hit_rate[1]:.2f}")


    Chris_Paul = new_df_1.where(new_df_1.player_name=='chris paul').select(col("player_name"),col("Zone"),col("SHOT_RESULT"))
    Paul_result = Chris_Paul.groupBy('Zone').agg(sum((Chris_Paul.SHOT_RESULT == 'made').cast('int')).alias('num_made'),count('*').alias('num_shot')).withColumn('hit_rate', col('num_made') / col('num_shot'))
    Paul_max_hit_rate = Paul_result.select('Zone', 'hit_rate').orderBy(desc('hit_rate')).first()
    print(f"Chris Paul: {Paul_max_hit_rate[0]}, hit rate: {Paul_max_hit_rate[1]:.2f}")


    Stephen_Curry = new_df_1.where(new_df_1.player_name=='stephen curry').select(col("player_name"),col("Zone"),col("SHOT_RESULT"))
    Curry_result = Stephen_Curry.groupBy('Zone').agg(sum((Stephen_Curry.SHOT_RESULT == 'made').cast('int')).alias('num_made'),count('*').alias('num_shot')).withColumn('hit_rate', col('num_made') / col('num_shot'))
    Curry_max_hit_rate = Curry_result.select('Zone', 'hit_rate').orderBy(desc('hit_rate')).first()
    print(f"Stephen Curry: {Curry_max_hit_rate[0]}, hit rate: {Curry_max_hit_rate[1]:.2f}")


    Lebron_James = new_df_1.where(new_df_1.player_name=='lebron james').select(col("player_name"),col("Zone"),col("SHOT_RESULT"))
    James_result = Lebron_James.groupBy('Zone').agg(sum((Lebron_James.SHOT_RESULT == 'made').cast('int')).alias('num_made'),count('*').alias('num_shot')).withColumn('hit_rate', col('num_made') / col('num_shot'))
    James_max_hit_rate = James_result.select('Zone', 'hit_rate').orderBy(desc('hit_rate')).first()
    print(f"Lebron James: {James_max_hit_rate[0]}, hit rate: {James_max_hit_rate[1]:.2f}")
    
    spark.stop()


