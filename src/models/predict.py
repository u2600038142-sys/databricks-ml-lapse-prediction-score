import argparse
import mlflow
from pyspark.sql import SparkSession
from src.utils.io import Paths

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="models:/customer_lapse_model/Production")
    args = parser.parse_args()

    spark = SparkSession.builder.getOrCreate()
    paths = Paths()

    # Load recent features (replace with UC source)
    df = spark.table(paths.feature_table)
    pdf = df.drop("customer_id").toPandas()

    model = mlflow.pyfunc.load_model(args.model)
    proba = model.predict(pdf)

    out = df.select("customer_id").toPandas()
    out["lapse_score"] = proba
    sdf = spark.createDataFrame(out)
    sdf.write.mode("overwrite").saveAsTable(paths.predictions_table)

if __name__ == "__main__":
    main()
