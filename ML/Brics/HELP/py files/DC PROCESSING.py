import findspark
findspark.init()
from pyspark import SparkContext
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, FloatType,TimestampType,StringType,IntegerType
from pyspark.sql.functions import col,udf,avg,PandasUDFType,pandas_udf
import pyspark.sql.functions as F

from pyspark.sql.types import *
from sqlalchemy import create_engine

import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt

conf = pyspark.SparkConf().setAll([("spark.driver.maxResultSize", '6g')])
conf.set("spark.executor.memory", "6g")
spark = SparkSession.builder.appName('brics').enableHiveSupport().master('spark://master:7077').getOrCreate()
data_spark = spark.sql('select * from brics.bears_4th_test')

from pyspark.sql.types import TimestampType

@pandas_udf(TimestampType(), PandasUDFType.SCALAR)
def time_udf(x):
    date_format = "%Y.%m.%d.%H.%M.%S"
    time_result = pd.to_datetime(x, format=date_format)
    return pd.Series(time_result)

# Apply FFT UDF to each 'bear' column
data_spark_clean = data_spark.withColumn(
    'time',time_udf(data_spark.time)
).orderBy('time','sequence')

from pyspark.sql.functions import col,udf,avg,PandasUDFType,pandas_udf
@pandas_udf("double",PandasUDFType.GROUPED_AGG)
def margi(x):
    return x - x.mean()

margin_factor = data_spark_clean.groupby('time').agg(
    margi(data_spark_clean.bear1).alias("bear1_margi"),
    margi(data_spark_clean.bear2).alias("bear2_margi"),
    margi(data_spark_clean.bear3).alias("bear3_margi"),
    margi(data_spark_clean.bear4).alias("bear4_margi")
    )

df = margin_factor.limit(100000).toPandas()
df = df.sort_values('time').reset_index(drop=True)
df.to_csv('/home/ec2-user/results/result1_3/result1_3.csv',index=False)