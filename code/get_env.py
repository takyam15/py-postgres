from dotenv import dotenv_values


config = dotenv_values(".env")

host = config['POSTGRES_HOST']
port = config['POSTGRES_PORT']
dbname = config['POSTGRES_DB']
user = config['POSTGRES_USER']
password = config['POSTGRES_PASSWORD']
