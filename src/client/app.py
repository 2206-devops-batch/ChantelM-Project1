# python3 -m flask run
# ctrl+c

from flask import Flask, render_template
from dotenv import dotenv_values
import psycopg2

config = dotenv_values(".env")
curenv = config['CURENV']
app = Flask(__name__, template_folder='./templates')

def get_db_connection():
    conn = None
    if curenv=='DEVELOPMENT':
        conn = psycopg2.connect(host=config['DB_DEV_HOST'],
                                port=config['DB_DEV_PORT'],
                                database=config['DB'],
                                user=config['DB_USER'],
                                password=config['DB_PASSWORD'])
    return conn


@app.route('/')
def hello():
    camps=['camp0']

    if curenv == 'DEVELOPMENT':
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('SELECT * FROM camps;')
            camps = cur.fetchall()
            cur.close()
            conn.close()
        except:
            camps = ['camp3', 'camp4']

    return render_template('index.html', camps=camps)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')