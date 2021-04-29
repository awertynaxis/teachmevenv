from typing import List
from typing import Dict
from typing import Tuple
import dataclasses
import typing
from itertools import *
import json
import random
import argparse

parser_password=argparse.ArgumentParser(prog='enter_password')
parser_password.add_argument('enter_password', metavar='ENTER_PASSWORD', nargs='+', type=str)
parser_password.add_argument('--autogenerate_password', dest='autogenerate_password', action='store_const', const=True)
parser_password.add_argument('--create_new_password', dest='create_new_password', action='store_const', const=True)
parser_password.add_argument('--autogenerate_hex', dest='autogenerate_hex', action='store_const', const=True)
args= parser_password.parse_args()


power = {'1': 'one',
         '2': 'two',
         '3': 'three',
         '4': 'four',
         '5': 'five',
         '6': 'six',
         '7': 'seven',
         '8': 'eight',
         '9': 'nine',
         '0': 'zero'
         }
sequense=[i for i in range(30)]
sequense.append('sa')
sequense.insert(4,'sada')


class IntegersInStrings:
     def __init__(self, sequense : List[int],power):
         self.__sequense = sequense
         self.__power=power

     def __iter__(self):
         return (1*item for item in self.__sequense)

     def iter_in(sequense : List[int])->List[str]:
        result=[]
        for item in sequense:
           if type(item)==type(2):
                item=str(item)
                iter_item=iter(item)
                for i in range(0,len(item)):
                    result.append(power[next(iter_item)])
        return result

     def join_result(self,result:List[str])->str:
         return ' '.join(result)


jonny = IntegersInStrings(sequense, power)
print(jonny.iter_in())
print(type(jonny.iter_in()))
print(jonny.join_result(jonny.iter_in()))


class DrunkStrings:
    """class with string object and has method
    wich shows any combinations of letters"""
    def __init__(self, sequense: str):
        self.__sequense = sequense

    def __iter__(self):
        return (print(''.join(item)) for item in permutations(self.__sequense))

with open('D:/teachmevenv/hakernews.txt',
              'r',
          encoding='utf-8') as f:
                bear = json.load(f)
count = 0
gear = DrunkStrings(bear[0]['author'])
for x in gear.__iter__():
    count += 1
print(count)


def random_generator(pls_stop: int) -> typing.Generator:
    """Create a generator wich dropes a random even number """
    limit = 0
    list_numbers = [x for x in range(201)]
    while limit <= pls_stop:
        char = random.choice(list_numbers)
        if char % 2 == 0:
            yield char
        else:
            yield 'mistake'
        limit += 1


for x in random_generator(200):
    print(next(random_generator(200)))


def join_generator(liist: List= [], diict: Dict={}, tuuple: Tuple=(), strings: str = '') -> List[typing.Any]:
        """Create a generator wich links any types of sequense"""
        result = []
        result.extend(liist)
        result.append(tuuple)
        result.extend(strings)
        result.append(tuple(diict.items()))
        yield result


tuuple = tuple(power.keys())
for x in join_generator(sequense, power, tuuple, bear[0]['title']):
      print(x)


@dataclasses.dataclass
class Squirrel:
    """Class describes squirrels"""
    name: str = 'unknown'
    type: str = 'degu'
    diet: str = 'feed'


def serializer_squirrel(self:Squirrel) -> str:
    """This function serialize a object type Squirrel into string"""
    serialized = []
    serialized.append(self.name)
    serialized.append(self.type)
    serialized.append(self.diet)
    return ' '.join(serialized)


@dataclasses.dataclass
class Islands:
    """Class describes islands on Earth planet"""
    name: str = 'unknown name'
    coordinates: str = 'unknown'
    size: int = 'unknown square'


def serializer_islands(self: Islands) -> str:
    """This function serialize a object type Islands into string"""
    serialized = []
    serialized.append(self.name)
    serialized.append(self.coordinates)
    serialized.append(str(self.size))
    return ' '.join(serialized)


@dataclasses.dataclass
class Maps:
    """Class describes battlefield maps"""
    name: str = 'unknown'
    rounds: int = 0
    vehicle: bool = True

def serializer_maps(self: Maps) -> str:
    """This function serialize a object type Maps into string"""
    serialized = []
    serialized.append(self.name)
    serialized.append(str(self.rounds))
    serialized.append(str(self.vehicle))
    return ' '.join(serialized)


Jacky = Squirrel('Jacky')
Sindy = Squirrel('Sindy', 'underwater', 'nuts')
Scrat = Squirrel('Scrat', 'squirrel+rat', 'acorns')
List_Squirrel=[Jacky, Sindy, Scrat]

Maldives = Islands('Maldives', '1 degree south longitude and 8 degree north longitude', 300)
Bora_bora = Islands('Bora-Bora', '151 degree east longitude and 16 degree south longitude', 38)
Island = Islands(coordinates='19 degree south longitude and 47 degree west longitude')
List_Islands = [Maldives, Bora_bora, Island]

Map_1 = Maps('Sunken Dragon', 254)
Map_2 = Maps('Lumphini garden', 340, False)
Map_3 = Maps('Nansha Strike', 123)
List_Maps = [Map_1, Map_2, Map_3]


def mixed_lists(list_1: List = [], list_2: List = [], list_3: List = []) -> List[typing.Any]:
    """This function takes 3 list object and if they have the same 'len':
    builds a list and fills it with  mixed elements of entered lists"""
    mix_list = []
    if len(list_1) == len(list_2) == len(list_3):
        for x in range(0, len(list_1)):
            mix_list.append(list_1.pop())
            mix_list.insert(0, list_2.pop())
            mix_list.insert(1, mix_list.pop())
            mix_list.append(list_3.pop())
        return mix_list
    else:
        raise RuntimeError(f'not right len of list {list_1}')


dict_classes = {Maps: serializer_maps,
                Islands: serializer_islands,
                Squirrel: serializer_squirrel
                }


def gen_secret(dict_classes: Dict, mixed_lists: typing.Callable) -> str:
    """This function create a generator object
     via using method choice of module secrets"""
    import secrets
    for x in mixed_lists(List_Maps, List_Islands, List_Squirrel):
        secret_prototype = dict_classes[type(x)](x)
        secret = secrets.choice(secret_prototype)
        if secret is not ' ':
            yield secret


def create_random_password(gen_secret:typing.Callable)->str:
    """This function is rotating generator and join it in string"""
    password=[]
    for x in gen_secret(dict_classes, mixed_lists):
        password.append(x)
    return ''.join(password)


def makes_hex(create_random_password: typing.Callable) -> hex:
    """This function transforming a string wich was returned
     by create_random_password function  into a hex"""
    import hashlib
    password = create_random_password(gen_secret)
    hex = hashlib.sha512(password.encode())
    hex_digest = hex.digest()
    return hex_digest


def hashed_password(password: str) -> hex:
    """Get a string type and create hex type object
    via using hashlib.sha256"""
    import uuid
    import hashlib
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode()+password.encode()).hexdigest()+':'+salt


def checking_password(password_hex:hex, user_password: str) -> bool:
    """Function checking 2 entered passwords and return bool value True/False"""
    import hashlib
    password, salt = password_hex.split(':')
    return password == hashlib.sha256(salt.encode()+user_password.encode()).hexdigest()


if args.autogenerate_password:
    print(create_random_password(gen_secret))
if args.autogenerate_hex:
    print(makes_hex(create_random_password))
if args.create_new_password:
    password_hex = hashed_password(args.enter_password[0])
    old_pass = input('Pls confirm password: ')
    if checking_password(password_hex, old_pass):
        print('Welcome Boss!')
        with open('D:/teachmevenv/passwords.txt',
             'w',
             encoding='utf-8') as f:
            f.writelines(password_hex)
    else:
        print('Ah shit, here we go again')
        with open('D:/teachmevenv/passwords.txt',
              'w',
              encoding='utf-8') as f:
            f.writelines(f'U didnt confirem a password{args.enter_password[0]}')