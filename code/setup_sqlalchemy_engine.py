from dotenv import dotenv_values
from sqlalchemy import create_engine


config = dotenv_values('.env')

host = config['POSTGRES_HOST']
port = config['POSTGRES_PORT']
dbname = config['POSTGRES_DB']
username = config['POSTGRES_USER']
password = config['POSTGRES_PASSWORD']

engine = create_engine(
    f'postgresql+psycopg://{username}:{password}@{host}:{port}/{dbname}'
)
