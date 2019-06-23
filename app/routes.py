from app import app
from flask import Flask
from app.forms import Addcard
from app.models import Game, Question, Answer
from lxml import etree
from app.newforms import UploadForm
from werkzeug import secure_filename
from flask import render_template, flash, redirect, url_for, request, abort, session

@app.route('/addcard', methods=['GET', 'POST'])
def addcard():
    AddCard = Addcard(prefix="AddCard")
    if AddCard.submit.data and AddCard.validate():
        file = AddCard.xml.data
        with open(file) as fobj:
            xml = fobj.read()
        game = Game(character=AddCard.character.data)
        db.session.add(game)
        db.session.commit()
        AuthorForm.character.data=''
    return render_template('addcard.html', Addcard=AddCard)



@app.route('/game', methods=['GET', 'POST'])
def game(Pid):
    return render_template("games.html")

@app.route('/konec', methods=['GET', 'POST'])
def konec():
    return render_template('konec.html')

@app.route('/games', methods=['GET', 'POST'])
def games():
    games = Game.query.all()
    length = len(games)
    return render_template('game.html', games=games, length=length)


@app.route('/addxml', methods=['GET', 'POST'])
def addxml():
    name = 'ede'
    file = request.files['inputF']
    name = file.filename
    a =  file.read()
    root = etree.fromstring(a)
    return render_template('xml.html', name=name)
