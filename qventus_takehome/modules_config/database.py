from dataclasses import dataclass
from qventus_takehome.modules_config.base import BaseSetting
from qventus_takehome.configuration import env
from qventus_takehome.exceptions import QventusSettingsException

@dataclass
class DatabaseSettings(BaseSetting):
    engine: str
    name: str
    user: str
    password: str
    host: str
    port: int = 3306
    

with env.prefixed("DB_"):
    ENGINE = env.str("ENGINE") 
    NAME = env.str("NAME")
    USER = env.str("USER")
    PASSWORD = env.str("PASSWORD")
    HOST = env.str("HOST") 
    PORT = env.str("PORT")

try:
    DATABASE_SETTINGS = DatabaseSettings(
        engine = ENGINE,
        name = NAME,
        user = USER,
        password = PASSWORD,
        host = HOST,
        port = PORT
    )
except Exception as e:
    raise QventusSettingsException("Database Settings wrongly configured") from e