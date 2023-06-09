# -*- coding: utf-8 -*-
"""Proj2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cFwC2hNsEeIlsf6kYHaxDAl9EAIT0tse
"""

from __future__ import print_function

import sys
import numpy as np

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import isnan, when, count, lit
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType, DoubleType

from pyspark.ml.linalg import Vector, Matrices
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

from pyspark.ml.stat import Correlation
from pyspark.mllib.stat import Statistics
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.evaluation import MulticlassMetrics

if __name__ == "__main__":
  spark = SparkSession\
    .builder\
    .appName("LogReg")\
    .getOrCreate()

  df=spark.read\
    .format("csv")\
    .option("inferSchema","true")\
    .option("header","true")\
    .load('/P2/Part2/input/framingham.csv') #*****change this line to sys.argv[1]

#####DATA PREP#####

  df=df.drop('education')
  df=df.na.drop() #checked for null values to make sure this worked

  #casting string dtype to double
  df = df.withColumn('cigsPerDay', df['cigsPerDay'].cast('double'))
  df = df.withColumn('BPMeds', df['BPMeds'].cast('double'))
  df = df.withColumn('totChol', df['totChol'].cast('double'))
  df = df.withColumn('BMI', df['BMI'].cast('double'))
  df = df.withColumn('heartRate', df['heartRate'].cast('double'))
  df = df.withColumn('glucose', df['glucose'].cast('double'))
  
  df = df.withColumn('bias', lit(1.0).cast('double'))


#####FEATURE SELECTION#####
  

  # convert to vector column first
  vector_col = "corr_features"
  assembler = VectorAssembler(inputCols=df.columns[:-1], outputCol=vector_col, handleInvalid ='skip')
  df_vector = assembler.transform(df).select(vector_col)

  # get correlation matrix
  matrix = Correlation.corr(df_vector, vector_col)
  arr = matrix.collect()[0]["pearson({})".format(vector_col)].values

  cols = len(df.columns)-1
  arr=arr.reshape((cols, cols)).tolist()

  rdd = spark.sparkContext.parallelize(arr)
  schema = StructType([
      StructField(df.columns[0], DoubleType(), True),
      StructField(df.columns[1], DoubleType(), True),
      StructField(df.columns[2], DoubleType(), True),
      StructField(df.columns[3], DoubleType(), True),
      StructField(df.columns[4], DoubleType(), True),
      StructField(df.columns[5], DoubleType(), True),
      StructField(df.columns[6], DoubleType(), True),
      StructField(df.columns[7], DoubleType(), True),
      StructField(df.columns[8], DoubleType(), True),
      StructField(df.columns[9], DoubleType(), True),
      StructField(df.columns[10], DoubleType(), True),
      StructField(df.columns[11], DoubleType(), True),
      StructField(df.columns[12], DoubleType(), True),
      StructField(df.columns[13], DoubleType(), True),
      StructField(df.columns[14], DoubleType(), True),  
  ])

  corr_df = spark.createDataFrame(rdd,schema)

  final_corrs=corr_df.rdd.map(lambda x: x[-1]).collect()
  inds=sorted(range(len(final_corrs)), key=lambda i: final_corrs[i])[-7:]
  final_cols=[]
  for ind in inds:
    if ind!=14:
      final_cols.append(df.columns[ind])

#####LOGISTIC REGRESSION#####

  columns=final_cols
  assembler = VectorAssembler(inputCols = columns, outputCol='features', handleInvalid='skip')
  df2 = assembler.transform(df)

  final_df = df2.select('features', 'TenYearCHD')
  train, test = final_df.randomSplit([0.8, 0.2])

  #logistic regression train & test
  lr = LogisticRegression(labelCol="TenYearCHD")
  lrn = lr.fit(train)
  lrn_summary = lrn.summary

  pred = lrn.transform(test)
  pred.select('TenYearCHD', 'features',  'rawPrediction', 'prediction', 'probability')
  accuracy = pred.filter(pred.TenYearCHD == pred.prediction).count() / float(pred.count())

  #####EVALUATION#####

  cm1 = pred.select('TenYearCHD', 'prediction')
  cm1=cm1.withColumn("TenYearCHD",cm1.TenYearCHD.cast(DoubleType()))

  l=[]
  for i in cm1.collect():
    l.append(tuple(i))

  eval_dset = spark.createDataFrame(l, ["raw", "label"])

  evaluator = BinaryClassificationEvaluator()
  evaluator.setRawPredictionCol("raw")
  AUC=evaluator.evaluate(eval_dset)

  predictionAndLabels = spark.sparkContext.parallelize(l)
  metrics = MulticlassMetrics(predictionAndLabels)

  confusion=metrics.confusionMatrix().toArray()
  FPR=round(metrics.falsePositiveRate(1.0),3)
  precision=round(metrics.precision(1.0),3)
  recall=round(metrics.recall(1.0),3)
  f_score=round(metrics.fMeasure(0.0, 1.0),3)


  #####LOWER THRESHOLD#####


#round 2
  thresh=.4

  lr_2 = LogisticRegression(labelCol="TenYearCHD")
  lrn_2 = lr_2.fit(train)
  lrn_2.setThreshold(thresh)
  lrn_2_summary = lrn_2.summary

  pred_2 = lrn_2.transform(test)
  pred_2.select('TenYearCHD', 'features',  'rawPrediction', 'prediction', 'probability')
  accuracy_2 = pred_2.filter(pred_2.TenYearCHD == pred_2.prediction).count() / float(pred_2.count())

  cm2 = pred_2.select('TenYearCHD', 'prediction')
  cm2=cm2.withColumn("TenYearCHD",cm2.TenYearCHD.cast(DoubleType()))

  l=[]
  for i in cm2.collect():
    l.append(tuple(i))
  
  eval_dset = spark.createDataFrame(l, ["raw", "label"])

  evaluator = BinaryClassificationEvaluator()
  evaluator.setRawPredictionCol("raw")
  AUC2=evaluator.evaluate(eval_dset)

  predictionAndLabels = spark.sparkContext.parallelize(l)
  metrics = MulticlassMetrics(predictionAndLabels)
  confusion2=metrics.confusionMatrix().toArray()
  recall2=round(metrics.recall(1.0),3)


#round 3
  thresh=.3

  lr_3 = LogisticRegression(labelCol="TenYearCHD")
  lrn_3 = lr_2.fit(train)
  lrn_3.setThreshold(thresh)
  lrn_3_summary = lrn_3.summary

  pred_3 = lrn_3.transform(test)
  pred_3.select('TenYearCHD', 'features',  'rawPrediction', 'prediction', 'probability')
  accuracy_3 = pred_3.filter(pred_3.TenYearCHD == pred_3.prediction).count() / float(pred_3.count())

  cm3 = pred_3.select('TenYearCHD', 'prediction')
  cm3=cm3.withColumn("TenYearCHD",cm3.TenYearCHD.cast(DoubleType()))

  l=[]
  for i in cm3.collect():
    l.append(tuple(i))
  
  eval_dset = spark.createDataFrame(l, ["raw", "label"])

  evaluator = BinaryClassificationEvaluator()
  evaluator.setRawPredictionCol("raw")
  AUC3=evaluator.evaluate(eval_dset)

  predictionAndLabels = spark.sparkContext.parallelize(l)
  metrics = MulticlassMetrics(predictionAndLabels)
  confusion3=metrics.confusionMatrix().toArray()
  recall3=round(metrics.recall(1.0),3)



#round 4
  thresh=.2

  lr_4 = LogisticRegression(labelCol="TenYearCHD")
  lrn_4 = lr_4.fit(train)
  lrn_4.setThreshold(thresh)
  lrn_4_summary = lrn_4.summary

  pred_4 = lrn_4.transform(test)
  pred_4.select('TenYearCHD', 'features',  'rawPrediction', 'prediction', 'probability')
  accuracy_4 = pred_4.filter(pred_4.TenYearCHD == pred_4.prediction).count() / float(pred_4.count())

  cm4 = pred_4.select('TenYearCHD', 'prediction')
  cm4=cm4.withColumn("TenYearCHD",cm4.TenYearCHD.cast(DoubleType()))

  l=[]
  for i in cm4.collect():
    l.append(tuple(i))
  
  eval_dset = spark.createDataFrame(l, ["raw", "label"])

  evaluator = BinaryClassificationEvaluator()
  evaluator.setRawPredictionCol("raw")
  AUC4=evaluator.evaluate(eval_dset)

  predictionAndLabels = spark.sparkContext.parallelize(l)
  metrics = MulticlassMetrics(predictionAndLabels)
  confusion4=metrics.confusionMatrix().toArray()
  recall4=round(metrics.recall(1.0),3)


#round 5
  thresh=.1

  lr_5 = LogisticRegression(labelCol="TenYearCHD")
  lrn_5 = lr_5.fit(train)
  lrn_5.setThreshold(thresh)
  lrn_5_summary = lrn_5.summary

  pred_5 = lrn_2.transform(test)
  pred_5.select('TenYearCHD', 'features',  'rawPrediction', 'prediction', 'probability')
  accuracy_5 = pred_5.filter(pred_5.TenYearCHD == pred_5.prediction).count() / float(pred_5.count())

  cm5 = pred_5.select('TenYearCHD', 'prediction')
  cm5=cm5.withColumn("TenYearCHD",cm5.TenYearCHD.cast(DoubleType()))

  l=[]
  for i in cm5.collect():
    l.append(tuple(i))
  
  eval_dset = spark.createDataFrame(l, ["raw", "label"])

  evaluator = BinaryClassificationEvaluator()
  evaluator.setRawPredictionCol("raw")
  AUC5=evaluator.evaluate(eval_dset)

  predictionAndLabels = spark.sparkContext.parallelize(l)
  metrics = MulticlassMetrics(predictionAndLabels)
  confusion5=metrics.confusionMatrix().toArray()
  recall5=round(metrics.recall(1.0),3)




#####PRINT#####
  print('Null values after drop na:')
  df.select([count(when(isnan(c), c)).alias(c) for c in df.columns]).show()

  print('Target variable outcome distribution:')
  df.groupby('TenYearCHD').count().show()

  #describe dataset
  print('Dataset description:')
  df.describe(['male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose', 'TenYearCHD']).show()

  print('Most highly correlated features:', final_cols)

#round 1
  print('Accuracy: ',round(accuracy, 3))
  print('Misclassification: ', round(1-accuracy, 3))
  print('AUC:',AUC)

  print('Confusion Matrix:\n', confusion)
  print('False positive rate:', FPR)
  print('Precision:', precision)
  print('Recall:', recall)
  print('F-score:', f_score)

#round 2
  print(f'\nLowering threshold to .4 ...\n')
  print('Accuracy: ',round(accuracy_2, 3))
  print('Misclassification: ', 1-round(accuracy_2, 3))
  print('AUC:',AUC2)
  print('Confusion Matrix:\n', confusion2)
  print('Recall:', recall2)

#round 3
  print(f'\nLowering threshold to .3 ...\n')
  print('Accuracy: ',round(accuracy_3, 3))
  print('Misclassification: ', 1-round(accuracy_3, 3))
  print('AUC:',AUC3)
  print('Confusion Matrix:\n', confusion3)
  print('Recall:', recall3)

#round 4
  print(f'\nLowering threshold to .2 ...\n')
  print('Accuracy: ',round(accuracy_4, 3))
  print('Misclassification: ', 1-round(accuracy_4, 3))
  print('AUC:',AUC4)
  print('Confusion Matrix:\n', confusion4)
  print('Recall:', recall4)

#round 5
  print(f'\nLowering threshold to .1 ...\n')
  print('Accuracy: ',round(accuracy_5, 3))
  print('Misclassification: ', 1-round(accuracy_5, 3))
  print('AUC:',AUC5)
  print('Confusion Matrix:\n', confusion5)
  print('Recall:', recall5)
