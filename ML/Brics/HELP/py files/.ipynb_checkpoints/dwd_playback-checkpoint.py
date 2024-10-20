import pyspark
from pyspark.sql import SparkSession
import pandas as pd
pd.set_option('display.max_columns', None)
pd.DataFrame.iteritems = pd.DataFrame.items

def time_list(time):
    return time.replace(':',', ')

def FetchHiveTable():
        fetch_sql = "select * from ods.user_playback_data"
        df = spark.sql(fetch_sql).toPandas()
        df_copy = df.copy()
        df_copy['playtime'] = df_copy['playtime'].apply(time_list)
        print(df_copy)
        df_copy = df_copy.groupby(['user_id', 'date', 'item_id']).apply(lambda x:x)
        df_copy['dwd_insert_user']='user1'
        df_copy['dwd_modify_user']='user1'
        df_copy.dropna(inplace=True)
        spark_df = spark.createDataFrame(df_copy)
        spark_df.write.mode("overwrite").saveAsTable("dwd.dim_user_playback_data")
        print(df_copy)

if __name__ == "__main__":
        appname = "ExtractCars"
        #Creating Spark Session
        spark = SparkSession.builder.master("local[*]").appName(appname).config("spark.sql.warehouse.dir", "/user/hive_remote/warehouse").config("hive.metastore.uris", "thrift://slave2:9083").enableHiveSupport().getOrCreate()
        print("Spark application name: " + appname)
        FetchHiveTable()
        spark.stop()
        exit(0)

