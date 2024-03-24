import pyspark
from pyspark.sql import SparkSession
import pandas as pd 
pd.set_option('display.max_columns', None)
pd.DataFrame.iteritems = pd.DataFrame.items
def FetchHiveTable():
        fetch_sql = "select * from ods.app_launch_logs"
        df = spark.sql(fetch_sql).toPandas()
        print(df.info())
        df_copy = df.copy()
        df_copy['type'] = df['date_load'] +', '+ df['launch_type']
        df_copy = df_copy.groupby('user_id',as_index=False)
        df_copy = df_copy.apply(lambda x:x)
        print(df_copy)
        df_copy['dwd_insert_user']='user1'
        df_copy['dwd_modify_user']='user1'
        df_copy.sort_values(by='user_id')
        df_copy.dropna(inplace=True)
        print(df_copy)
        spark_df = spark.createDataFrame(df_copy)
        spark_df.write.mode("overwrite").saveAsTable("dwd.dim_app_launch_logs")
        print(spark_df.show())

if __name__ == "__main__":
        appname = "ExtractCars"
        #Creating Spark Session
        spark = SparkSession.builder.master("local[*]").appName(appname).config("spark.sql.warehouse.dir", "/user/hive_remote/warehouse").config("hive.metastore.uris", "thrift://slave2:9083").enableHiveSupport().getOrCreate()
        print("Spark application name: " + appname)
        FetchHiveTable()
        spark.stop()
        exit(0)
