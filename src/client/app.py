from flask import Flask, flash, render_template, request
from flask_bootstrap import Bootstrap
from utils.forms import AddCampgroundForm, DelCampgroundForm
import utils.db as db
import sys

app = Flask(__name__, template_folder='./templates')
Bootstrap(app)
app.config['SECRET_KEY'] = db.config.APP_SECRET_KEY


dummies = [('1', 'a', '123'), ('2', 'b', '123')]
@app.route('/',  methods=['GET', 'POST'])
def homepage():
    addForm = AddCampgroundForm()
    delForm = DelCampgroundForm()
    
    if request.method == 'POST':
        if addForm.submitA.data and addForm.validate():
            res = db.add_campground(addForm.campName.data, addForm.campLocation.data)
            print(f'add res: {res}', file=sys.stdout)

        elif delForm.submitD.data and delForm.validate():
            res = db.del_campground(delForm.campNum.data)
            print(f'del res: {res}', file=sys.stdout)

    return render_template('home.html', addForm=addForm, delForm=delForm, camps=db.get_all_campgrounds())

if __name__ == '__main__':
    options = [True, '0.0.0.0', '5000']

    app.run(debug=options[0], host=options[1], port=options[2])