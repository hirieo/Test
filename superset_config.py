import os

user = os.getenv("POSTGRES_USER")
passwd = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")
db = os.getenv("POSTGRES_DB")

auth = f"{user}:{passwd}" if passwd else user

SQLALCHEMY_DATABASE_URI = f"cockroachdb://{auth}@{host}:{port}/{db}?sslmode=disable"

# does not work because of string compare for version extract fails
#SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{auth}@{host}:{port}/{db}"