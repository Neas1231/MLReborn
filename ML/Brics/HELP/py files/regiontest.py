import pyspark
from pyspark.sql.functions import desc, asc
from pyspark.sql import SparkSession
import pandas as pd
pd.set_option('display.max_columns', None)
pd.DataFrame.iteritems = pd.DataFrame.items
def FetchHiveTable():
        fetch_sql = 'select * from dwd.dim_user_portrait_data'
        spark_df = spark.sql(fetch_sql)
        print(spark_df.groupBy(['territory_code','device_type']).count().orderBy(asc('territory_code')).show())
        fetch_sql = 'select * from dwd.dim_user_playback_data'
        spark_df = spark.sql(fetch_sql)


if __name__ == "__main__":
        appname = "Hive"
        #Creating Spark Session
        spark = SparkSession.builder.master("local[*]").appName(appname).config("spark.sql.warehouse.dir", "/user/hive_remote/warehouse").config("hive.metastore.uris", "thrift://slave2:9083").enableHiveSupport().getOrCreate()
        print("Spark application name: " + appname)
        FetchHiveTable()
        spark.stop()
        exit(0)
