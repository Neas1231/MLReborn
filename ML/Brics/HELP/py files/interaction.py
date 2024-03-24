import pyspark
from pyspark.sql import SparkSession
import pandas as pd
pd.set_option('display.max_columns', None)
pd.DataFrame.iteritems = pd.DataFrame.items
def date_tonum(date):
    date = str(date)
    print(date)
    date = date[0:date.find(' ')]
    date = date.replace('-','')
    return int(date)

def FetchHiveTable():
        fetch_sql = "select * from ods.user_interaction_data"
        df = spark.sql(fetch_sql).toPandas()
        df_copy = df.sort_values(by='id')
        df_copy['dwd_insert_user']='user1'
        df_copy['dwd_modify_user']='user1'
        df_copy.dropna(inplace=True)
        df_copy['date'] = df_copy['date'].apply(date_tonum)
        spark_df = spark.createDataFrame(df_copy)
        spark_df.write.mode("overwrite").saveAsTable("dwd.dim_user_interaction_data")
        print(spark_df.printSchema())
        print(spark_df.show())

if __name__ == "__main__":
        appname = "ExtractCars"
        spark = SparkSession.builder.master("local[*]").appName(appname).config("spark.sql.warehouse.dir", "/user/hive_remote/warehouse").config("hive.metastore.uris", "thrift://slave2:9083").enableHiveSupport().getOrCreate()
        FetchHiveTable()
        spark.stop()
        exit(0)
