import pyspark
from pyspark.sql import SparkSession
import pandas as pd
pd.set_option('display.max_columns', None)
pd.DataFrame.iteritems = pd.DataFrame.items
def FetchHiveTable():
        fetch_sql = "select * from ods.video_related_data"
        df = spark.sql(fetch_sql).toPandas()
        df_copy = df.groupby('item_id').apply(lambda x:x)
        df_copy.dropna(inplace=True)
        df_copy['all']=''
        for col in df_copy.drop(columns='all').columns:
            df_copy['all'] =df_copy['all'] + ', ' + df_copy[f'{col}'].apply(str)
        df_copy['dwd_insert_user']='user1'
        df_copy['dwd_modify_user']='user1'
        df_copy = df_copy[['item_id','all','dwd_insert_user','dwd_modify_user']]
        spark_df = spark.createDataFrame(df_copy)
        spark_df.write.mode("overwrite").saveAsTable("dwd.dim_video_related_data")
        print(spark_df.show())

if __name__ == "__main__":
        appname = "ExtractCars"
        #Creating Spark Session
        spark = SparkSession.builder.master("local[*]").appName(appname).config("spark.sql.warehouse.dir", "/user/hive_remote/warehouse").config("hive.metastore.uris", "thrift://slave2:9083").enableHiveSupport().getOrCreate()
        print("Spark application name: " + appname)
        FetchHiveTable()
        spark.stop()
        exit(0)
