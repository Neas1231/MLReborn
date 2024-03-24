import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import concat, col, lit, asc, monotonically_increasing_id, udf
import pandas as pd
from pyspark.sql.types import ArrayType, StringType, StructField, StructType
pd.set_option('display.max_columns', None)
pd.DataFrame.iteritems = pd.DataFrame.items

def FetchHiveTable():
        fetch_sql = "select * from ods.user_playback_data"
        spark_df = spark.sql(fetch_sql)
        time_replace = udf(lambda x:x.replace(':',', '))
        spark_df = spark_df.withColumn('playtime',time_replace(spark_df['playtime']))
        spark_df = spark_df.withColumn('id',monotonically_increasing_id())
        spark_df = spark_df.sort('user_id','date','item_id','id')
        spark_df = spark_df.withColumn('dwd_insert_user',lit('user1'))
        spark_df = spark_df.withColumn('dwd_modify_user',lit('user1'))
        #spark_df = spark.createDataFrame(df_copy)
        #spark_df.write.mode("overwrite").saveAsTable("dwd.dim_user_playback_data")
        print(spark_df.show())

if __name__ == "__main__":
        appname = "ExtractCars"
        #Creating Spark Session
        spark = SparkSession.builder.master("local[*]").appName(appname).config("spark.sql.warehouse.dir", "/user/hive_remote/warehouse").config("hive.metastore.uris", "thrift://slave2:9083").enableHiveSupport().getOrCreate()
        print("Spark application name: " + appname)
        FetchHiveTable()
        spark.stop()
        exit(0)

