import argparse
import mlflow
from pyspark.sql import SparkSession
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.data.loader import load_training_data
from src.data.features import build_features

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", action="store_true")
    parser.add_argument("--experiment", type=str, default=None)
    args = parser.parse_args()

    spark = SparkSession.builder.getOrCreate()

    if args.experiment:
        mlflow.set_experiment(args.experiment)

    with mlflow.start_run():
        raw = load_training_data(spark)
        feats = build_features(raw)

        pdf = feats.select("tenure_months","support_tickets","discount_util","tickets_per_month","is_new","lapsed").toPandas()
        X = pdf.drop(columns=["lapsed"]).values
        y = pdf["lapsed"].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        mlflow.sklearn.autolog()
        pipe = Pipeline([
            ("scaler", StandardScaler()),
            ("clf", LogisticRegression(max_iter=500))
        ])
        pipe.fit(X_train, y_train)

        preds = pipe.predict_proba(X_test)[:,1]
        auc = roc_auc_score(y_test, preds)
        mlflow.log_metric("auc", auc)

        if args.register:
            model_info = mlflow.sklearn.log_model(pipe, "model")
            mlflow.register_model(model_info.model_uri, name="customer_lapse_model")

if __name__ == "__main__":
    main()
