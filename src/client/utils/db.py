import psycopg2
import os
import utils.env as config
# import env as config

curenv = os.environ.get('FLASK_ENV')

def set_host_port():
    if curenv == 'production':
        return config.DB_PROD_HOST, config.DB_PROD_PORT
    
    return config.DB_DEV_HOST, config.DB_DEV_PORT

DB_HOST, DB_PORT = set_host_port()

def get_db_connection():
    conn = None
    try:
        conn = psycopg2.connect(
                                host=DB_HOST,
                                port=DB_PORT,
                                user=config.DB_USER,
                                password=config.DB_PASSWORD)
    except:
        conn = None
    
    return conn


def get_all_campgrounds():
    conn = get_db_connection()
    campgrounds = None

    if conn is None:
        return ['Unable to connect']
    
    try:
        cur = conn.cursor()
        cur.execute("select * from campgrounds")
        campgrounds = cur.fetchall()
        cur.close()
        conn.close()
    except:
        campgrounds = ['Unable to find table']
    
    return campgrounds

def add_campground(cName, cLocation):
    pass

def del_campground(cNum):
    conn = get_db_connection()

    if conn is None:
        return ['Unable to connect']
    
    try:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM campgrounds WHERE id = {cNum}")
        conn.commit()
        cur.close()
        conn.close()
    except:
        return False
    
    return True