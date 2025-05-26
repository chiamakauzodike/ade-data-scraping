import os
from dotenv import load_dotenv

# load the .env file
load_dotenv()

# configuration variables
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT_MYSQL = int(os.environ.get("DB_PORT_MYSQL", 3307))
DB_PORT_POSTGRESQL = os.environ.get("DB_PORT_POSTGRESQL")
DB_PORT_SQLSERVER = os.environ.get("DB_PORT_SQLSERVER")
MSSQL_SA_PASSWORD = os.environ.get("MSSQL_SA_PASSWORD")


if not DB_PASSWORD:
    raise EnvironmentError("Missing db_password env variable.")

if not DB_USERNAME:
    raise EnvironmentError("Missing db_username env variable.")

if not DB_NAME:
    raise EnvironmentError("Missing db_name env variable.")

if not DB_HOST:
    raise EnvironmentError("Missing db_host env variable.")
