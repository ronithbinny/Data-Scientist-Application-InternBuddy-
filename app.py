from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,IntegerField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
import pandas as pd
import numpy as np
from catboost import CatBoostClassifier


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    name = TextField("Enter Name : ")
    mob = IntegerField("Enter Mobile Number : ")
    deg = SelectField("Degree? : ", choices = [("B.Tech","B.Tech"),("B.Tech","B.E"),("M.Tech","M.Tech"),("M.Tech","M.Sc"),("-","None Of Above")], default = 0)
    year_of_grad = IntegerField("Year Of Gradution : ")
    python = SelectField("Pyhton, on scale of 1 to 3? : ", choices = [("1","1"),("2","2"),("3","3"),("0","Dont Know")], default = 0)
    R = SelectField("R, on scale of 1 to 3? : ", choices = [("1","1"),("2","2"),("3","3"),("0","Dont Know")], default = 0)
    datasci = SelectField("Data Science, on scale of 1 to 3? : ", choices = [("1","1"),("2","2"),("3","3"),("0","Dont Know")], default = 0)
    ml = SelectField("Do you know Machine Learning? : ", choices = [("0","No"),("1","Yes")], default = 0)
    dl = SelectField("Do you know Deep Learning? : ", choices = [("0","No"),("1","Yes")], default = 0)
    aws = SelectField("Do you know AWS? : ", choices = [("0","No"),("1","Yes")], default = 0)
    nlp = SelectField("Do you know NLP? : ", choices = [("0","No"),("1","Yes")], default = 0)
    sm = SelectField("Do you know Stastical Modeling? : ", choices = [("0","No"),("1","Yes")], default = 0)
    sql = SelectField("Do you know SQL/NoSQL? : ", choices = [("0","No"),("1","Yes")], default = 0)
    excel = SelectField("Do you know Excel? : ", choices = [("0","No"),("1","Yes")], default = 0)



    submit = SubmitField("SUBMIT")


@app.route('/', methods = ['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['name'] = (form.name.data)
        session['mob'] = (form.mob.data)
        session['deg'] = (form.deg.data)
        session['year_of_grad'] = (form.year_of_grad.data)
        session['python'] = (form.python.data)
        session['R'] = (form.R.data)
        session['datasci'] = (form.datasci.data)
        session['ml'] = (form.ml.data)
        session['dl'] = (form.dl.data)
        session['aws'] = (form.aws.data)
        session['nlp'] = (form.nlp.data)
        session['sm'] = (form.sm.data)
        session['sql'] = (form.sql.data)
        session['excel'] = (form.excel.data)






        X_O = ([ int(session['python']), int(session['R']), int(session['datasci']), (int(session['ml']) + int(session['dl']) + int(session['aws'])
        + int(session['nlp']) + int(session['sm']) + int(session['sql']) + int(session['excel']) ), session['deg'], int(session['year_of_grad'])  ])

        print(X_O)

        pred = []
        import model
        pred.append(model.Predict(X_O))

        if pred[0] == 1 :
            res = "Congrats! You Have Been Selected!"
        else :
            res = "Sorry! Better Luck Next Time"

        return render_template("predict.html",pred=res)



    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
