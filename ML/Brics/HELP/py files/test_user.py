import pyspark
from pyspark.sql.functions import concat, col, lit, asc, monotonically_increasing_id
from pyspark.sql import SparkSession
import pandas as pd
pd.set_option('display.max_columns', None)
pd.DataFrame.iteritems = pd.DataFrame.items
def FetchHiveTable():
        fetch_sql = "select * from ods.user_portrait_data"
        spark_df = spark.sql(fetch_sql)
        spark_df = spark_df.dropDuplicates()
        spark_df = spark_df.withColumn('dwd_insert_user',lit('user1'))
        spark_df = spark_df.withColumn('dwd_modify_user',lit('user1'))
        spark_df = spark_df.dropna()
        #spark_df.write.partitionBy('territory_code').mode("overwrite").saveAsTable("dwd.dim_user_portrait_data")
        print(spark_df.show())

if __name__ == "__main__":
        appname = "ExtractCars"
        #Creating Spark Session
        spark = SparkSession.builder.master("local[*]").appName(appname).config("spark.sql.warehouse.dir", "/user/hive_remote/warehouse").config("hive.metastore.uris", "thrift://slave2:9083").enableHiveSupport().getOrCreate()
        print("Spark application name: " + appname)
        FetchHiveTable()
        spark.stop()
        exit(0)

