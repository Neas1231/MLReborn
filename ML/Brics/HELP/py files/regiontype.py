import pyspark
from pyspark.sql import SparkSession
import pandas as pd
pd.set_option('display.max_columns', None)
pd.DataFrame.iteritems = pd.DataFrame.items
def FetchHiveTable():
        fetch_sql = "select * from dwd.dim_user_portrait_data"
        df = spark.sql(fetch_sql).toPandas()
        df_copy = df.groupby(['territory_code','device_type']).count()
        terr = list(map(lambda x : x[0],df_copy.index))
        typ = list(map(lambda x:x[1],df_copy.index))
        total = df_copy['age']
        region_df = pd.DataFrame({'territory_code':terr,'device_type':typ,'user_total':total})
        print(region_df)
        spark_df = spark.createDataFrame(region_df)
        spark_df.write.mode("overwrite").format("jdbc").option("driver","com.mysql.cj.jdbc.Driver").option("url", "jdbc:mysql://localhost:3306/dws").option("dbtable", "regiontype").option("user", "root").option("password", "Pwd666666").save()
        print(spark_df.show())

if __name__ == "__main__":
        appname = "Hive"
        #Creating Spark Session
        spark = SparkSession.builder.master("local[*]").appName(appname).config("spark.sql.warehouse.dir", "/user/hive_remote/warehouse").config("hive.metastore.uris", "thrift://slave2:9083").enableHiveSupport().getOrCreate()
        print("Spark application name: " + appname)
        FetchHiveTable()
        spark.stop()
        exit(0)
