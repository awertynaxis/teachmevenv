import requests
import json
import pprint
import math
import re
import sys

def input_number()->int:
    """Get a number of titles wich have to parsed """
    number=input('Pls input how many titles do u want to get: ')
    return int(number)


def calculate(input_number)->int:
    """ Calculate a number of pages wich should be parsed"""
    pages=math.ceil(input_number()/30)
    return pages

BASE_URL = 'https://news.ycombinator.com/'

def get_page(page: int = 1) -> str:
    """Returns html of specified hacker news feed `page`"""
    assert page >= 1

    url = BASE_URL
    if page > 1:
        url = f'{BASE_URL}?p={page}'

    return requests.get(url).text


url_re=r'"(?P<url>https?:\/\/.*?)"\s'
author_re=r'"user\?id=(?P<author>\w*)'
title_re=r'class="storylink"\s?(rel="nofollow")?>(?P<title>.*?)</a'
score_re=r'class="score"\sid=".*?">(?P<score>.*?)<'
comments_re=r'>(?P<comments>\d*)&nbsp;comments'

def Devider_html(get_page,calculate)->list:
    """This function get html page and divide it for bloks"""
    result = []
    for x in range(1,calculate(input_number)+1):
        HTML_RE = re.findall(r'(<td\salign.*\s*.*)', get_page(x))
        result.extend(looking_keys(HTML_RE))
    return result



def looking_keys(HTML_RE:list)->list:
    """Function gets a list of information and parse it by using regular expressions,
    result is list every element of it is dict wich contains key/value(parsed via regular expressions )"""
    key_mapper=[]
    for line in HTML_RE:
        KEY_MAPPER={}
        url = re.search(r'"(?P<url>https?:\/\/.*?)"\s', line)
        if url != None:
            KEY_MAPPER['url'] = url.group('url')
        author = re.search(r'"user\?id=(?P<author>\w*)', line)
        if author != None:
            KEY_MAPPER['author'] = author.group('author')
        title = re.search(r'class="storylink"\s?(rel="nofollow")?>(?P<title>.*?)</a', line)
        if title != None:
            KEY_MAPPER['title'] = title.group('title')
        score = re.search(r'class="score"\sid=".*?">(?P<score>.*?)<', line)
        if score != None:
            KEY_MAPPER['score'] = score.group('score')
        comments = re.search(r'>(?P<comments>\d*)&nbsp;comments', line)
        if comments != None:
            KEY_MAPPER['comments'] = comments.group('comments')

        key_mapper.append(KEY_MAPPER)
    return key_mapper


def drope_result(Devider_html,input_number)->list:
    """Function returns a number of titles wich were called"""
    drop= []
    number_titles=input_number()
    List=Devider_html(get_page,calculate)
    for x in range(number_titles):
        drop.append(List[x])
    return drop


def back_top(drope_result,input_number)->list:
    """procces a result of function drope_result and create a list wich contains only 'author' and 'score'"""
    suit_drop=[]
    element=drope_result(Devider_html,input_number)
    for x in range(input_number()):
        drop = []
        drop.append(element[x]['author'])
        drop.append(looking_number(element[x]['score']))
        suit_drop.append(drop)
    return suit_drop

def looking_number(*args)->int:
    ''''search and return int value'''
    number=re.findall(r'\d{1,}',*args)
    return int(number[0])


def sorting(back_top):
    """sortes a result of performance back_top function"""
    sort=sorted(back_top(drope_result,input_number),key=lambda s:(-s[1]))
    return sort


def write_read(*args):
    '''function write data in json format date in file and load it '''
    if args[0]=='write':
        with open('D:/teachmevenv/hakernews.txt',
           'w',
           encoding='utf-8') as f:
            json.dump(drope_result(Devider_html,input_number),f,indent=4)
    if args[0]=='read':
        with open('D:/teachmevenv/hakernews.txt',
              'r',
              encoding='utf-8') as f:
            tar=json.load(f)
            pprint.pprint(tar[0:input_number()])

argument = sys.argv[1:]
allowed_commands = ['news', 'top', 'write', 'read']
print(argument)
cmd=argument[0]
if cmd not in allowed_commands:
    raise RuntimeError(f'not allowed command{cmd}')
if cmd =='news':
    print(drope_result(Devider_html, input_number))
if cmd=='top':
    print(sorting(back_top))
if cmd=='write':
    write_read(cmd)
if cmd=='read':
    write_read(cmd)