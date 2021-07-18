import environ
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, backref
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.sql import func
import datetime

env = environ.Env()
env.read_env()

DB_PASSWORD: str = env.str('DB_PASS')
DB_USER: str = env.str('DB_USER')
DB_NAME: str = env.str('DB_NAME')
DB_HOST: str = env.str('DB_HOST')
DB_PORT: str = env.str('DB_PORT')
DB_ECHO: bool = env.bool('DB_ECHO')
#
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=DB_ECHO)
print(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


if not database_exists(engine.url):
    create_database(engine.url)

BaseModel = declarative_base()


class Magazine(BaseModel):
    __tablename__ = 'magazine'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=False)
    group = relationship('Group', foreign_keys='Magazine.group_id', backref='groups')
    students_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    students = relationship('Student', foreign_keys='Magazine.students_id', backref='students')


class Group(BaseModel):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    group_name = Column(String)


class Student(BaseModel):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    second_name = Column(String)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=False)
    group = relationship('Group', foreign_keys='Student.group_id', backref='groupss')


class StudentAndBooks(BaseModel):
    __tablename__ = 'students and books'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    second_name = Column(String)


class Schedule(BaseModel):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    books = relationship('Books', foreign_keys='Schedule.book_id', backref=backref('bookes', uselist=False))


association_table = Table(
    'association',
    BaseModel.metadata,
    Column('students and books_id', Integer, ForeignKey('students and books.id')),
    Column('books_id', Integer, ForeignKey('books.id'))
    )


class Books(BaseModel):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    book_name = Column(String)
    author = Column(String)
    students = relationship('StudentAndBooks', secondary=association_table, backref='books')


BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
status_was = 'Person was'
status_wasnt = 'Person wasnt'
group_firs = '10705114'
group_second = '10705214'
date = [datetime.date(2021, 2, 9), datetime.date(2021, 3, 9), datetime.date(2021, 4, 9)]
students = [['Anton', 'Semenenko', group_firs, status_was],
            ['Ivan', 'Lagunovich', group_firs, status_wasnt],
            ['Maxim', 'Kovalenko', group_firs, status_was],
            ['Vladimir', 'Konanov', group_firs, status_was],
            ['Alexey', 'Gordel', group_firs, status_wasnt],
            ['Algima', 'Semenenko', group_second, status_was],
            ['Julia', 'Adamovich', group_second, status_wasnt],
            ['Dmitry', 'Shupenko', group_second, status_wasnt],
            ['Yaroslav', 'Romanovsky', group_second, status_wasnt],
            ['Aleksandr', 'Osipov', group_second, status_was],
            ]
for day in date:
    for human in students:
        group = Group(group_name=human[2])
        unit = Student(name=human[0], second_name=human[1], group=group)
        magazine = Magazine(date=day, group=group, students=unit, status=human[3])
        session.add_all([magazine, group, unit])
status_count = session.query(Magazine).filter_by(status='Person was').count()
print(status_count)
date_status_count = session.query(Magazine).filter_by(status='Person was', date='2021,4,9').count()
print(date_status_count)
units = [StudentAndBooks(name='Anton', second_name='Semenenko'),
        StudentAndBooks(name='Algima', second_name='Semenenko'),
        StudentAndBooks(name='Ivan', second_name='Lagunovich'),
        StudentAndBooks(name='Vladimir', second_name='Konanov'),
        StudentAndBooks(name='Julia', second_name='Adamovich'),
        StudentAndBooks(name='Dmitriy', second_name='Shupenko'),
         ]
book_list = [['Feast for crows', 'George Raymond Richard Martin'],
             ['Philosophers stone', 'Joanne Rowling'],
             ['Chamber of secrets', 'Joanne Rowling'],
             ['Dance with dragon', 'George Raymond Richard Martin'],
             ['Artemis Fowl', 'Eoin Colfer'],
             ]
for day in date:
    for composition in book_list:
        book = Books(book_name=composition[0], author=composition[1], students=units)
        twenty_four_hours = Schedule(books=book, date=day)
        session.add_all([book, twenty_four_hours])
date_use = session.query(StudentAndBooks).filter_by(name='Algima').first()
for x in date_use.books:
    print(x.book_name)
    print(x.author)
    print(x.bookes.date)
session.commit()
