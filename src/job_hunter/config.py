import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    scan_interval_minutes: int = int(os.getenv("SCAN_INTERVAL_MINUTES", "60"))
    minimum_match_score: int = int(os.getenv("MINIMUM_MATCH_SCORE", "80"))
    maximum_distance_km: int = int(os.getenv("MAXIMUM_DISTANCE_KM", "25"))
    minimum_salary_eur: int = int(os.getenv("MINIMUM_SALARY_EUR", "0"))
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///data/job_hunter.db")

settings = Settings()
