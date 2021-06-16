#!/usr/bin/env python
import typing

from flask import Flask, redirect, url_for, request, render_template
import datetime
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
from PostgresSQL_DB import engine

my_app = Flask(__name__)
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'postgres'
DB_HOST = 'postgres'
DB_ECHO = True

my_app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
db = SQLAlchemy(my_app)


class Player(db.Model):
    id = db.Column('player_id', db.Integer, primary_key=True)
    nick_name = db.Column(db.String(100))
    country = db.Column(db.String(50))
    team = db.Column(db.String(200))
    rank = db.Column(db.String(10))

    def __init__(self, nick_name, country, team, rank):
        self.nick_name = nick_name
        self.country = country
        self.team = team
        self.rank = rank


class Registration(db.Model):
    mailbox = db.Column(db.String, primary_key=True)
    password = db.Column(db.String(500))
    nick_name = db.Column(db.String(100))

    def __init__(self, mailbox, password, nick_name):
        self.mailbox = mailbox
        self.password = password
        self.nick_name = nick_name


def hashing(password: str) -> str:
    import hashlib
    hax = hashlib.sha256(password.encode())
    hex_digets = hax.digest()
    return str(hex_digets)


def inquiry(mailbox: str, password: str) -> Registration:
    return Registration.query.filter_by(mailbox=mailbox, password=hashing(password)).first()


def inquiry_mailbox(mailbox: str) -> Registration:
    return Registration.query.filter_by(mailbox=mailbox).first()


if not database_exists(db.engine.url):
    create_database(db.engine.url)

db.init_app(my_app)
db.create_all()

Session = sessionmaker(bind=engine)
session = Session()


@my_app.route('/')
def hello_algima():
    return 'Hello Algima!'


@my_app.route('/bf6', strict_slashes=True)
def bf_6():
    return 'Game wasnt announced yet'


@my_app.route('/date', strict_slashes=True)
def date():
    return str(datetime.date.today().strftime("%d /%m /%Y"))


@my_app.route('/players/<string:playername>')
def welcome_to_home(playername: str):
    return f'Hello {playername} we glad to see u again solder'


@my_app.route('/<string:number_first>/<string:operator>/<string:number_second>')
def calculate(number_first: str, number_second: str, operator: str):
    registry = {'sum': '+',
                'minus': '-',
                'mul': '*',
                'div': '/',
                'diventire': '//',
                'remainder': '%',
                'degreup': '**'
                }
    if operator in registry:
        return str(eval(f'{number_first}{registry[operator]}{number_second}'))
    else:
        return f'Entered {operator} is not supported in this calculator or u make mistake,' \
               f' pls check supported list operators: {", ".join(registry.keys())} '


@my_app.route('/word/<string:word>')
def word_handling(word: str):
    if len(word) % 2 != 0:
        return word[0::2]
    else:
        return word


@my_app.route('/success/<string:name>/<string:second_name>/<string:comment>')
def success(name, second_name, comment):
    return f'welcome user {name}  {second_name}, this is your comment:{comment} '


@my_app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_name = request.form['name']
        user_second_name = request.form['second']
        user_comment = request.form['comment']
        return redirect(url_for('success', name=user_name, second_name=user_second_name, comment=user_comment))
    else:
        return render_template('login.html')


@my_app.route('/stats/<string:nick_name>')
def stats(nick_name):
    if Player.query.filter_by(nick_name=nick_name).first():
        player = Player.query.filter_by(nick_name=nick_name).first()
        return f'Welcome,here it is information about {nick_name} : country:{player.country},'\
            f'  team:{player.team}, rank:{player.rank}'
    else:
        return f' Current player {nick_name} is not in our DataBase'


@my_app.route('/players', methods=['POST', 'GET'])
def players():
    if request.method == 'POST':
        nick_name = request.form['nick_name']
        return redirect(url_for('stats', nick_name=nick_name))
    else:
        return render_template('players.html')


@my_app.route('/battlestats', methods=['POST', 'GET'])
def battlestats():
    if request.method == 'POST':
        return redirect(url_for('authorization'))
    else:
        return render_template('welcome.html')


@my_app.route('/authorization', methods=['POST', 'GET'])
def authorization():
    if request.method == 'POST':
        mailbox = request.form['mailbox']
        password = request.form['password']
        if inquiry_mailbox(mailbox) is None:
            return redirect(url_for('registration'))
        if inquiry(mailbox, password):
            return redirect(url_for('players'))
        else:
            return redirect(url_for('wrong_password'))
    else:
        return render_template('authorization.html')


@my_app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        mailbox = request.form['mailbox']
        if inquiry_mailbox(mailbox):
            return f' This mail is already used, pls use another one'
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        nick_name = request.form['nick_name']
        if password == password_confirm:
            user = Registration(mailbox=mailbox, password=hashing(password), nick_name=nick_name)
        else:
            return f'Passwords is not equal'
        session.add(user)
        session.commit()
        return redirect(url_for('battlestats'))
    else:
        return render_template('registration.html')


@my_app.route('/wrong_password', methods=['POST', 'GET'])
def wrong_password():
    if request.method == 'POST':
        return redirect(url_for('authorization'))
    else:
        return render_template('wrongpassword.html')


def legendary_player():
    return 'awerty_naxis is worlds top class'


session.commit()
my_app.add_url_rule('/awerty_naxis', 'awerty_naxis', legendary_player)
my_app.run(host='0.0.0.0')
