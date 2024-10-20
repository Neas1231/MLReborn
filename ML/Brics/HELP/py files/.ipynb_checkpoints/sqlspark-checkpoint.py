from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
pd.set_option('display.max.columns',None)
pd.DataFrame.iteritems = pd.DataFrame.items


spark = SparkSession \
        .builder \
        .appName('test') \
        .master('local[*]') \
        .config("spark.driver.extraClassPath", "/opt/spark/jars/mysql-connector-j-8.1.0.jar") \
        .getOrCreate()
df = spark.read.format("jdbc").option("url","jdbc:mysql://master/dws").option("driver","com.mysql.jdbc.Driver").option("dbtable","regiontype").option("user","root").option("password","Pwd666666").load()

#spark_df = spark.createDataFrame(df)
#spark_df.write.mode("overwrite").saveAsTable("dws.regionavgpt")
df.show()
print(target_encoding_spark('device_type',df))
spark.stop()
exit(0)
