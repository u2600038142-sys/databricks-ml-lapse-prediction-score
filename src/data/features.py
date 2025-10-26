from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def build_features(df: DataFrame) -> DataFrame:
    return (
        df.withColumn("tickets_per_month", F.col("support_tickets")/F.col("tenure_months"))
          .withColumn("is_new", (F.col("tenure_months") < 3).cast("int"))
    )
