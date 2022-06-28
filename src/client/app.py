from flask import Flask, render_template
from dotenv import dotenv_values
import psycopg2
import os


curenv = os.environ.get('FLASK_ENV')
config = dotenv_values(".env")
# curenv = config['CURENV']
app = Flask(__name__, template_folder='./templates')

def get_db_connection():
    conn = None
    if curenv=='development':
        conn = psycopg2.connect(host=config['DB_DEV_HOST'],
                                port=config['DB_DEV_PORT'],
                                database=config['DB'],
                                user=config['DB_USER'],
                                password=config['DB_PASSWORD'])
    return conn


@app.route('/')
def hello():
    camps=['campA', 'campB']
    conn = get_db_connection()

    if conn is not None:
        camps = ['successful link']
        # try:
        #     cur = conn.cursor()
        #     cur.execute('SELECT * FROM camps;')
        #     camps = cur.fetchall()
        #     cur.close()
        #     conn.close()
        # except:
        #     camps = ['camp3', 'camp4']

    return render_template('index.html', camps=camps)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')