from pyspark.sql import SparkSession
import pandas as pd
import numpy as np
pd.set_option('display.max.columns',None)
pd.DataFrame.iteritems = pd.DataFrame.items
import sqlalchemy
from sqlalchemy import text

def create_db_connection(host="master", database="dws"):
    return sqlalchemy.create_engine(
        f"mysql+pymysql://root:Pwd666666@{host}:3306/{database}"
    )
e = create_db_connection()
with e.connect() as con:
    query = "SELECT * FROM regiontype"
    df = pd.read_sql(query, con)
    spark = SparkSession.builder.appName('Hive').getOrCreate()
    spark_df = spark.createDataFrame(df)
    print(spark_df.show())
