import dataclasses
from typing import List
import os
import json
import argparse

parser_sign=argparse.ArgumentParser(prog='show_sign')
parser_sign.add_argument('show_sign', metavar='SHOW_SIGN', nargs='+', type=str)
parser_sign.add_argument('--name', dest='name', action='store_const', const=True)
parser_sign.add_argument('--gender', dest='gender', action='store_const', const=True)
parser_sign.add_argument('--location', dest='location', action='store_const', const=True)
parser_sign.add_argument('--status', dest='status', action='store_const', const=True)
parser_sign.add_argument('--species', dest='species', action='store_const', const=True)
args= parser_sign.parse_args()


file_path='D:/teachmevenv/rick_and_morty.txt'

def get_characters(page:int=1):
    '''This function makes a request for url page '''
    import requests
    url = 'https://rickandmortyapi.com/api/character/?page=1'
    if page>1:
        url=f'{url}?p={page}'

    return requests.get(url).json()['results']

if not os.path.exists(file_path):
    with open(file_path,
              'w',
              encoding='utf8') as f:
        fork=[]
        for x in range(1,35):
             fork.extend(get_characters(x))
        json.dump(fork,f)
else:
    with open(file_path,
              'w',
              encoding='utf8') as f:
        fork=[]
        for x in range(1,35):
             fork.extend(get_characters(x))
        json.dump(fork,f)
    with open(file_path,
              'r',
              encoding='utf8') as f:
           list_result=json.load(f)



@dataclasses.dataclass
class Character:
    """Class based on signs for characters from rick and morty movie"""
    gender: str='unknown'
    location: str='unknown'
    name:str='unknown'
    species:str='unknown'
    status:str='Alive'

def drope_characters(list_result:List[dict])->List[Character]:
    """This functions gets a list wich was loaded from file via
    json and create a class Character for every element of list"""
    character_lists=[]
    for x in range(0, len(list_result)):
        character = Character(list_result[x]['gender'], list_result[x]['location']['name'], list_result[x]['name'],
        list_result[x]['species'], list_result[x]['status'])
        character_lists.append(character)
    return character_lists


all_characters = drope_characters(list_result)


def creator_list_charactes(list_result : List[dict])->List[Character]:
    """This function create a class object Character and adds it for list,returns list"""
    character_list=[]
    for x in range(0, len(list_result)):
        character = Character(list_result[x]['gender'], list_result[x]['location']['name'], list_result[x]['name'],
        list_result[x]['species'], list_result[x]['status'])
        character_list.append(character)
    return character_list

def creator_full_list_charactes(creator_list_charactes:list)->List[Character]:
    """Function creates a list of result function get_characters"""
    full_charactes_list=[]
    for x in range (1,35):
        list_result = get_characters(x)
        full_charactes_list.extend(creator_list_charactes(list_result))
    return full_charactes_list



@dataclasses.dataclass
class Aggregator:
     """This class gets a list of Characters and makes aggregation of mutual sign"""

     all_characters:List[str]=dataclasses.field(default_factory=[])

     def show_charates(self,all_charactes:List)->list:
         show=[]
         for x in all_charactes:
            show.append(x.name)
         return show

     def show_status(self,all_charactes:list)->list:
         show=[]
         for x in all_charactes:
             show.append(x.status)
         return show

     def show_location(self,all_charactes:list)->list:
         show=[]
         for x in all_charactes:
             show.append(x.location)
         return show

     def show_gender(self,all_charactes:list)->list:
         show=[]
         for x in all_charactes:
             show.append(x.gender)
         return show
     def show_species(self,all_charactes:list)->list:
         show=[]
         for x in all_charactes:
             show.append(x.species)
         return show


@dataclasses.dataclass
class Wraper():
     """This class has methods to wrap a Aggregator class"""

     def is_all(self,cmd:str)->dict:
         folly = Aggregator(all_characters)
         check = {'show_status': folly.show_status(all_characters),
                  'show_gender': folly.show_gender(all_characters),
                  'show_location': folly.show_location(all_characters),
                  'show_species': folly.show_species(all_characters)
                  }
         Dict=dict.fromkeys(check[cmd],0)
         for x in check[cmd]:
            Dict[x]+=1
         return Dict


     def is_part_of_all(self,is_all:dict,comd:str,cmd:str)->dict:
         return self.is_all(cmd)[comd]


sing=Aggregator(all_characters)
sings=Wraper()
if args.location:
    if len(args.show_sign)==1:
        print(sing.show_location(all_characters))
        print(sings.is_all(args.show_sign[0]))
    else:
        molly=sings.is_part_of_all(sings.is_all, (' '.join(args.show_sign[1:])), args.show_sign[0])
        print(' '.join(args.show_sign[1:])+' '+str(molly))
if args.status:
    if len(args.show_sign)==1:
        print(sing.show_status(all_characters))
        print(sings.is_all(args.show_sign[0]))
    else:
        molly = sings.is_part_of_all(sings.is_all, (' '.join(args.show_sign[1:])), args.show_sign[0])
        print(' '.join(args.show_sign[1:]) + ' ' + str(molly))
if args.gender:
    if len(args.show_sign)==1:
        print(sing.show_gender(all_characters))
        print(sings.is_all(args.show_sign[0]))
    else:
        molly = sings.is_part_of_all(sings.is_all, (' '.join(args.show_sign[1:])), args.show_sign[0])
        print(' '.join(args.show_sign[1:]) + ' ' + str(molly))
if args.species:
    if len(args.show_sign)==1:
        print(sing.show_species(all_characters))
        print(sings.is_all(args.show_sign[0]))
    else:
        molly = sings.is_part_of_all(sings.is_all, (' '.join(args.show_sign[1:])), args.show_sign[0])
        print(' '.join(args.show_sign[1:]) + ' ' + str(molly))
if args.name:
    print(set(sing.show_charates(all_characters)))