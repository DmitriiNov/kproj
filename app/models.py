from datetime import datetime
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy_imageattach.entity import Image, image_attachment



QueAns = db.Table('que_ans',
    db.Column("QueId", db.Integer, ForeignKey("question.id")),
    db.Column("AnsId", db.Integer, ForeignKey("answer.id")))

class Game(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(80), unique=False)
    text = db.Column(db.String(200), unique=False)
    firstqID = db.Column(db.Integer, ForeignKey("question.id"), unique=True)
    firstq = db.relationship("Question", uselist=False, back_populates="first")

class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400), unique=False)
    first = db.relationship("Game", back_populates="firstq")
    next = db.relationship("Answer", back_populates="nextQ")
    answers = db.relationship("Answer", secondary=QueAns, back_populates="questions")

class Answer(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=False)
    nextqID = db.Column(db.Integer, ForeignKey("question.id"), unique=True)
    nextQ = db.relationship("Question", uselist=False, back_populates="next")
    questions = db.relationship("Question", secondary=QueAns, back_populates="answers")
