from pyspark.sql import SparkSession
from src.data.features import build_features

def test_build_features_smoke():
    spark = SparkSession.builder.master("local[1]").getOrCreate()
    df = spark.createDataFrame([(1, 2, 4)], ["customer_id","tenure_months","support_tickets"])
    out = build_features(df)
    cols = set(out.columns)
    assert {"tickets_per_month","is_new"}.issubset(cols)
