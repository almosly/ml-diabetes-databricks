from dataclasses import dataclass


@dataclass
class DataConfig:
    catalog: str = "training"
    schema: str = "default"
    table: str = "diabet_data"

    @property
    def full_table_name(self) -> str:
        return f"{self.catalog}.{self.schema}.{self.table}"


@dataclass
class TrainingConfig:
    target_column: str = "Outcome"  
    test_size: float = 0.2
    random_state: int = 42