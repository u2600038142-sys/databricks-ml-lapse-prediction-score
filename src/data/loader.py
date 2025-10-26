from pyspark.sql import SparkSession, DataFrame

def load_training_data(spark: SparkSession) -> DataFrame:
    # TODO: Replace with your UC source (tables/files). This is synthetic placeholder data.
    data = [
        (1, 12, 3, 0.2, 0),
        (2, 2, 10, 0.8, 1),
        (3, 8, 5, 0.4, 0),
        (4, 1, 12, 0.9, 1),
    ]
    cols = ["customer_id", "tenure_months", "support_tickets", "discount_util", "lapsed"]
    return spark.createDataFrame(data, cols)
