from dataclasses import dataclass
import os

@dataclass
class Paths:
    catalog: str = os.getenv("UC_CATALOG", "main")
    schema: str = os.getenv("UC_SCHEMA_DEV", "lapse_dev")

    @property
    def feature_table(self) -> str:
        return f"{self.catalog}.{self.schema}.customer_lapse_features"

    @property
    def predictions_table(self) -> str:
        return f"{self.catalog}.{self.schema}.customer_lapse_predictions"
