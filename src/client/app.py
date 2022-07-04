from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from utils.forms import SignupForm, LoginForm
import utils.db as db, utils.user as user

app = Flask(__name__, template_folder='./templates')
Bootstrap(app)
app.config['SECRET_KEY'] = db.config.APP_SECRET_KEY


@app.route('/')
def homepage():
    return render_template('home.html', camps=db.get_all_campgrounds())


if __name__ == '__main__':
    options = [False, db.config['AWS_HOST'], db.config['AWS_PORT']] if db.curenv == 'production' else [True, '0.0.0.0', '5000']

    app.run(debug=options[0], host=options[1], port=options[2])