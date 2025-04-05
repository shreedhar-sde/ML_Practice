# Install pyspark
# !pip install pyspark

# Resources
# https://spark.apache.org/docs/latest/sql-ref-functions-builtin.html#date-and-timestamp-functions
# https://spark.apache.org/docs/latest/sql-ref-functions-builtin.html#string-functions


# Problem statement: Gather sunrise and sunset data from weather api


# Extract Job
import requests
import concurrent.futures

def fetch_data(day):
    url = f"https://api.sunrise-sunset.org/json?lat=18.5204&lng=73.8567&date={day}"
    response = requests.get(url)
    if response.status_code == 200:
      rec_data=response.json()
      rec_data['day']=day
    return rec_data if response.status_code == 200 else {day:None}

day = ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20', '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30', '2024-01-31', '2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04', '2024-02-05', '2024-02-06', '2024-02-07', '2024-02-08', '2024-02-09', '2024-02-10', '2024-02-11', '2024-02-12', '2024-02-13', '2024-02-14', '2024-02-15', '2024-02-16', '2024-02-17', '2024-02-18', '2024-02-19', '2024-02-20', '2024-02-21', '2024-02-22', '2024-02-23', '2024-02-24', '2024-02-25', '2024-02-26', '2024-02-27', '2024-02-28', '2024-02-29']# Example range
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_data, day))
# Filter out failed requests
data = [str(res).replace(" ", "") for res in results if res]

#Transform Sql
spark_sql_1="""
select convert_timezone('UTC', 'Asia/Kolkata', a.sunrise) as sunrise_ist
,convert_timezone('UTC', 'Asia/Kolkata',a.sunset) as sunset_ist
,(unix_timestamp(sunset_ist) - unix_timestamp(sunrise_ist))/3600 as diff
from
(

SELECT to_timestamp(data.day||' '||data.results.sunrise, 'yyyy-MM-dd hh:mm:ss') as sunrise
,to_timestamp(data.day||' '||data.results.sunset, 'yyyy-MM-dd hh:mm:ss') as sunset
 FROM sun_data
 ) a
 order by sunrise_ist desc
"""

#Transform Job
from ctypes import Array
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, regexp_replace
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType, MapType
import requests
import json

# Create a SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.sql.legacy.timeParserPolicy", "LEGACY") \
    .getOrCreate()

schema=StructType([
    StructField("results",StructType([
        StructField("sunrise",StringType(),True),
        StructField("sunset",StringType(),True)
    ]),True),
    StructField("day",StringType(),True)
])

df=spark.createDataFrame([(s,) for s in data],["val"])
json_df = df.select(from_json(col("val"), schema).alias("data"))
json_df.createOrReplaceTempView("sun_data")
result_df=spark.sql(spark_sql_1)
result_df.show()
spark.stop()