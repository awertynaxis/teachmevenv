from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import argparse
import typing
import environ
parser_table = argparse.ArgumentParser(prog='enter_franchise_title_author')
parser_table.add_argument('enter_franchise_title_author', metavar='ENTER_FRANCHISE_TITLE_AUTHOR', nargs='+', type=str)
parser_table.add_argument('--check_password', dest='check_password', action='store_const', const=True)
parser_table.add_argument('--insert', dest='insert', action='store_const', const=True)
parser_table.add_argument('--delete', dest='delete', action='store_const', const=True)
parser_table.add_argument('--update', dest='update', action='store_const', const=True)
parser_table.add_argument('--select', dest='select', action='store_const', const=True)
parser_table.add_argument('--count', dest='count', action='store_const', const=True)
args = parser_table.parse_args()

env = environ.Env()
env.read_env()
DB_PASSWORD: str = env.str('DB_PASS')


def hashed_password(password: str) -> hex:
    """Get a string type and create hex type object
    via using hashlib.sha256"""
    import uuid
    import hashlib
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode()+password.encode()).hexdigest()+':'+salt


def checking_password(password_hex: hex, user_password: str) -> bool:
    """Function checking 2 entered passwords and return bool value True/False"""
    import hashlib
    password, salt = password_hex.split(':')
    return password == hashlib.sha256(salt.encode()+user_password.encode()).hexdigest()


HASH_BD_PASSWORD = hashed_password(DB_PASSWORD)
DB_NAME = 'library.db'


sql = create_engine(f'sqlite:///{DB_NAME}')
sql.execute("""
create table if not exists client(
id integer primary key autoincrement,
person_name varchar,
age integer
)
""")

# sql.execute("""
# insert into client (person_name,age)
# values ('Anton', 26)
# """)
# result=sql.execute("""select * from client""")
# # sql.execute("""upgrade """)
# for x in result:
#     print(x)
connection = sql.connect()
transaction = connection.begin()
# connection.execute("""
# insert into client(person_name,age,second_name)
# values (:person_name,:age,:person_name)
# """, person_name='Marvin', age=31,second_name='Monty'
# )
connection.execute("""
update client 
set second_name = 'Kolesnikov'
where id = 10
""")
connection.execute("""
delete from client 
where person_name is 'Marvin'
""")
connection.execute("""
update client 
set age = 24
where  person_name is 'Algima'
""")
transaction.commit()
connection.close()
for x in sql.execute("""select person_name from client where age<=51 and age>25 """):
    print(x)

engine = create_engine(f'sqlite:///{DB_NAME}', echo=False)
BaseModel = declarative_base()


class Books(BaseModel):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    franchise = Column(String)
    book_name = Column(String)
    author = Column(String)

    def __init__(self, franchise, book_name, author):
        self.franchise = franchise
        self.book_name = book_name
        self.author = author


author_1 = 'George Raymond Richard Martin'
author_2 = 'Joanne Rowling'
author_3 = 'Eoin Colfer'
Game_of_thrones = [Books('Game of Thrones', 'Feast for crows', author_1),
                   Books('Game of Thrones', 'Dance with dragon', author_1),
                   Books('Game of Thrones', 'Winds of winter', author_1),
                   Books('Game of Thrones', 'Dream of spring', author_1)]
Harry_Potter = [Books('Harry Potter', 'Philosophers stone', author_2),
                Books('Harry Potter', 'Chamber of secrets', author_2),
                Books('Harry Potter', 'Prisoner of Azkaban', author_2),
                Books('Harry Potter', 'Goblet of fire', author_2),
                Books('Harry Potter', 'Order of the Phoenix', author_2),
                Books('Harry Potter', 'Half-blood prince', author_2),
                Books('Harry Potter', 'Deathly hallows', author_2)]
Artemis_Fowl = [Books('Artemis Fowl', 'Artemis Fowl', author_3),
                Books('Artemis Fowl', 'The arctic incident', author_3),
                Books('Artemis Fowl', 'The eternity code', author_3),
                Books('Artemis Fowl', 'The opal deception', author_3),
                Books('Artemis Fowl', 'The lost colony', author_3),
                Books('Artemis Fowl', 'The time paradox', author_3),
                Books('Artemis Fowl', 'The Atlantis Complex', author_3)]
result = Game_of_thrones+Harry_Potter+Artemis_Fowl
BaseModel.metadata.create_all(engine)

Session_start = sessionmaker(bind=engine)
session = Session_start()
session.execute("""
update book 
set book_name = 'Game of Thrones'
where  id = 1
""")
person = session.query(Books).filter_by(franchise='Artemis Fowl').count()
# session.delete(person)
# session.add_all(result)
session.commit()


def select(key: str) -> typing.Any:
    """This function get string type object like key and checks it dict , if it is found returns a query object"""
    selection = {'franchise': session.query(Books).filter_by(franchise=args.enter_franchise_title_author[1]),
                 'book_name': session.query(Books).filter_by(book_name=args.enter_franchise_title_author[1]),
                 'author': session.query(Books).filter_by(author=args.enter_franchise_title_author[1])
                 }
    return selection[key]


if args.check_password:
    old_pass = input('Pls confirm password: ')
    if checking_password(HASH_BD_PASSWORD, old_pass):
        Session_start = sessionmaker(bind=engine)
        session = Session_start()
        if args.insert:
            session.add(Books(args.enter_franchise_title_author[0], args.enter_franchise_title_author[1],
                              args.enter_franchise_title_author[2]))
        if args.delete:
            result = select(args.enter_franchise_title_author[0])
            session.delete(result.first())
            print('Object has been deleted successfully')
        if args.select:
            result = select(args.enter_franchise_title_author[0])
            print((result.first()).franchise)
            print((result.first()).book_name)
            print((result.first()).author)
        if args.update:
            session.execute("""
            update book 
            set book_name = enter_franchise_title_author[1]
            where franchise = args.enter_franchise_title_author[0]
            """)
            session.execute("""
            update book
            set author =  enter_franchise_title_author[2]
            where franchise = args.enter_franchise_title_author[0]
            """)
        if args.count:
            result = select(args.enter_franchise_title_author[0])
            print(f'Number of {args.enter_franchise_title_author[0]} {args.enter_franchise_title_author[1]} is {result.count()}')
        session.commit()
        print(f'procedure {session.commit} finished successfully')
    else:
        print(f'{old_pass} is not validate password')
else:
    print('Sorry,we have to verificate password to allow u makes changes in DB, use --check_password')
