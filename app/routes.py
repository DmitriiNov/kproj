from app import app
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


@app.route('/', methods=['GET', 'POST'])
def game():
    games = ['Полицейский','Чиновник', 'Учитель\nмужчина', 'Учитель\nженщина', 'Врач']
    count = len(games)
    return render_template('game.html', count=count, games=games)

@app.route('/games', methods=['GET', 'POST'])
def games():
    return render_template('games.html')

@app.route('/konec', methods=['GET', 'POST'])
def konec():
    return render_template('konec.html')

@app.route('/addxml', methods=['GET', 'POST'])
def addxml():
    name = 'ede'
    file = request.files['inputF']
    name = file.filename
    with open(file.stream) as fobj:
        xml = fobj.read()
    return render_template('xml.html', name=name)
