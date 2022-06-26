# python3 -m flask run
# ctrl+c

from flask import Flask, render_template
import datetime
import psycopg2

app = Flask(__name__, template_folder='./templates')

def get_db_connection():
    conn = psycopg2.connect(host='testnet',
                            port='5432',
                            database='test',
                            user='postgres',
                            password='password')
    return conn


@app.route('/')
def hello():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM camps;')
    camps = cur.fetchall()
    cur.close()
    conn.close()
    print(camps)
    return render_template('index.html', camps=camps)

if __name__ == '__main__':
    # helps expose container to localhost
    app.run(debug=True, host='0.0.0.0')