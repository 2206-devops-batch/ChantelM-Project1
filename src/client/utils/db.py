from dotenv import dotenv_values
import psycopg2
import os

curenv = os.environ.get('FLASK_ENV')
config = dotenv_values(".env")

# DB_HOST = config['DB_PROD_HOST'] if curenv == 'production' else config['DB_DEV_HOST']
# DB_PORT = config['DB_PROD_PROD'] if curenv == 'production' else config['DB_DEV_PORT']

def get_db_connection():
    conn = None
    try:
        conn = psycopg2.connect(
                                # host=DB_HOST,
                                # port=DB_PORT,
                                database=config['DB'],
                                user=config['DB_USER'],
                                password=config['DB_PASSWORD'])
    except:
        conn = None
    
    return conn


def create_user_visited():
    pass

def create_user_wishlist():
    pass

def create_user():
    pass