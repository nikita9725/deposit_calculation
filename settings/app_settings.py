from pydantic import BaseSettings, Field

from features import load_json


class Config(BaseSettings):
    log_path: str = Field(default='logs', env='LOG_PATH')
    flask_app_config: dict = {'JSON_SORT_KEYS': False}

class Schemas:
    deposit_calc: dict = load_json('schemas/DepositCalcSchema.json')

config = Config()
schemas = Schemas()
