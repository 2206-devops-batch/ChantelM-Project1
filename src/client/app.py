from flask import Flask, render_template
from dotenv import dotenv_values
import psycopg2
import os


curenv = os.environ.get('FLASK_ENV')
config = dotenv_values(".env")
DB_HOST = config['DB_PROD_HOST'] if curenv == 'production' else config['DB_DEV_HOST']
DB_PORT = config['DB_PROD_PROD'] if curenv == 'production' else config['DB_DEV_PROD']

app = Flask(__name__, template_folder='./templates')


def get_db_connection():
    conn = None
    try:
        conn = psycopg2.connect(host=DB_HOST,
                                port=DB_PORT,
                                database=config['DB'],
                                user=config['DB_USER'],
                                password=config['DB_PASSWORD'])
    except:
        conn = None
    
    return conn


@app.route('/')
def hello():
    camps=['campA', 'campB']
    conn = get_db_connection()

    if conn is not None:
        cur = conn.cursor()
        cur.execute('SELECT * FROM users;')
        camps = cur.fetchall()
        cur.close()
        conn.close()

    return render_template('index.html', camps=camps)

if __name__ == '__main__':
    options = [False, config['AWS_HOST'], config['AWS_PORT']] if curenv != 'development' else [True, '0.0.0.0', '5000']

    app.run(debug=options[0], host=options[1], port=options[2])