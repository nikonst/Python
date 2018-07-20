from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from wtforms import Form, RadioField

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    imgsrc = "static/coppola.jpg"
    return render_template('about.html', imgsrc = imgsrc)

@app.route('/godfatherI')
def godfatherI():
    f = open('static/gf1.txt','r')
    text = f.read()
    f.close()
    imgsrc = "static/gf1.jpg"
    return render_template('godfatherI.html', text = text, imgsrc = imgsrc)

@app.route('/godfatherII')
def godfatherII():
    f = open('static/gf2.txt', 'r')
    text = f.read()
    f.close()
    imgsrc = "static/gf2.jpg"
    return render_template('godfatherII.html', text = text, imgsrc = imgsrc)

@app.route('/godfatherIII')
def godfatherIII():
    f = open('static/gf3.txt', 'r')
    text = f.read()
    f.close()
    imgsrc = "static/gf3.jpg"
    return render_template('godfatherIII.html', text = text, imgsrc = imgsrc)

class voteForm(Form):
    vote = RadioField('Vote', choices=[('godfather','The Godfather'),('godfather2','The Godfather II'),
                                       ('godfather3','The Godfather III')])

@app.route('/vote', methods=['GET','POST'])
def vote():
    form = voteForm(request.form)
    if request.method == 'POST' and form.validate():
        vote = form.vote.data
        print(vote)
        voteslist = []

        #Votes File
        votesfile = open("static/votes.txt", "r")
        for line in votesfile:
            print(int(line))
            voteslist.append(int(line))
        votesfile.close()
        if vote == "godfather":
            voteslist[0] += 1
        elif vote == "godfather2":
            voteslist[1] += 1
        elif vote == "godfather3":
            voteslist[2] += 1
        votesout = open("static/votes.txt", "w")
        for item in voteslist:
            votesout.write(str(item) + "\n")
        votesout.close()
        # Votes File

        return redirect(url_for("about"))
    return render_template('vote.html', form=form)

@app.route('/voteresults')
def voteresults():
    voteslist = []
    votesfile = open("static/votes.txt", "r")
    for line in votesfile:
        print(int(line))
        voteslist.append(int(line))
    votesfile.close()
    return render_template('votesresult.html', gf1 = voteslist[0], gf2 = voteslist[1], gf3 = voteslist[2])


if __name__ == '__main__':
    app.secret_key='theSecretKey'
    app.run(debug=True)