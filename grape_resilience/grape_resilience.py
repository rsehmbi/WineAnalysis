#!/usr/bin/env python3

import sys
from pyspark.sql import SparkSession, functions, types
from internal_error import InternalError, print_error



spark = SparkSession.builder.appName('Grape Resilience').getOrCreate()
spark.sparkContext.setLogLevel('WARN')

assert sys.version_info >= (3, 5) # make sure we have Python 3.5+
assert spark.version >= '2.4' # make sure we have Spark 2.4+

data_schema = types.StructType([
    types.StructField("FullName", types.StringType()), # Winery + wine name + year
    types.StructField("Winery", types.StringType()),
    types.StructField("WineName", types.StringType()),
    types.StructField("Year", types.IntegerType()),
    types.StructField("Region", types.StringType()),
    types.StructField("RegionalVariety", types.StringType()), # Varietal?
    types.StructField("VintageRating", types.FloatType()), # Average rating for vintage
    types.StructField("VintageRatingCount", types.IntegerType()), 
    types.StructField("WineRating", types.FloatType()), # Average rating across vintages
    types.StructField("WineRatingCount", types.IntegerType()), 
    types.StructField("VintagePrice", types.FloatType()), # Same as below
    types.StructField("WinePrice", types.FloatType()), # GBP/750ml
    types.StructField("VintageRatingPrice", types.FloatType()), # rating/price
    types.StructField("WineRatingPrice", types.FloatType()) # rating/price
    ])


def main():
    data = spark.read.csv("white-wine-price-rating.csv", header = True, schema = data_schema)
    data.show()


if __name__=='__main__':
    try:
        main()
    except InternalError as error:
        print_error(error)
    except Exception as error:
        print("Unhandled exception: " + str(error))
