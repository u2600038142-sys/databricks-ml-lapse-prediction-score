from pyspark.sql import SparkSession
from src.data.loader import load_training_data
from src.data.features import build_features

def test_train_data_shapes():
    spark = SparkSession.builder.master("local[1]").getOrCreate()
    df = build_features(load_training_data(spark))
    assert df.count() > 0
