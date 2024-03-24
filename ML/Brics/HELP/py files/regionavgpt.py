from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
pd.set_option('display.max.columns',None)
pd.DataFrame.iteritems = pd.DataFrame.items

def play_sec(time):
    indices = [i for i, x in enumerate(time) if x == ',']
    first = int(time[:indices[0]])*3600
    second = int(time[indices[0]+2:indices[1]])*60
    third = int(time[indices[1]+2:])
    return first+second+third

def low_high(arr):
    Q1 = int(arr.quantile(0.25))
    Q3 = int(arr.quantile(0.75))
    print(Q1,Q3)
    work = pd.cut(arr, [0, Q1, Q3, np.inf], labels=['low','same','high'])
    return work
appname = 'Hive'
spark = SparkSession.builder.appName(appname).config("spark.sql.warehouse.dir", "/user/hive_remote/warehouse").config("hive.metastore.uris","thrift://slave2:9083").enableHiveSupport().getOrCreate()

sql_req = "SELECT * FROM dwd.dim_user_playback_data"
df = spark.sql(sql_req).toPandas()
print(df)
playtime = df['playtime'].apply(play_sec)
grad = low_high(playtime)
df['grad'] = grad

spark_df = spark.createDataFrame(df)
spark_df.write.mode("overwrite").saveAsTable("dws.regionavgpt")
spark_df.show()

spark.stop()
exit(0)
