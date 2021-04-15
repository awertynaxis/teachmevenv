import requests
import pprint
BASE_URL = 'https://news.ycombinator.com/'

import re

def input_number()->int:
    """Get a number of titles wich have to parsed """
    number=input('Pls input how many titles do u want to get: ')
    return int(number)

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

GET_INFO_RE=(rf'(?P<url>{url_re}'
             rf'(?P<author>{author_re}'
             rf'(?P<title>{title_re}'
             rf'(?p<score>{score_re}'
             rf'?P<comments>{comments_re}'
             )


GET_INFO_R=(r'"(?P<url>https?:\/\/.*?)"\s'
            r'"user\?id=(?P<author>\w*)'
            r'class="storylink"\s?(rel="nofollow")?>(?P<title>.*?)</a'
            r'class="score"\sid=".*?">(?P<score>.*?)<'
            r'>(?P<comments>\d*)&nbsp;comments'
            )


KEY_MAPPER={
    'url':None,
    'author':None,
    'title':None,
    'score':None,
    'comments': lambda comments_str: comments_str+' comments'
}

def devider_html(get_page)->list:

    HTML_RE = re.findall(r'(<td\salign.*\s*.*)', get_page(1))

    result=[]

    for line in HTML_RE:
        if match:=re.search(GET_INFO_RE,line):
            result.append(parser(match))
    return print(result)

def parser(request_match:re.Match)->dict:

    result={}
    for key,mapper in KEY_MAPPER.items():
        if group :=request_match.group(key):
            result[key]=mapper(group) if mapper else group
    return result

#devider_html(get_page)


def Devider_html(get_page)->list:


    HTML_RE = re.findall(r'(<td\salign.*\s*.*)', get_page(1))

    result=[]

    for line in HTML_RE:
        KEY_MAPPER={}
        url=re.search(r'"(?P<url>https?:\/\/.*?)"\s',line)
        if url!=None:
            KEY_MAPPER['url']=url.group('url')
        author=re.search(r'"user\?id=(?P<author>\w*)',line)
        if author!=None:
            KEY_MAPPER['author']=author.group('author')
        title=re.search(r'class="storylink"\s?(rel="nofollow")?>(?P<title>.*?)</a',line)
        if title!=None:
            KEY_MAPPER['title']=title.group('title')
        score=re.search( r'class="score"\sid=".*?">(?P<score>.*?)<',line)
        if score!=None:
            KEY_MAPPER['score']=score.group('score')
        comments=re.search(r'>(?P<comments>\d*)&nbsp;comments',line)
        if comments!=None:
            KEY_MAPPER['comments']=comments.group('comments')

        result.append(KEY_MAPPER)
    return result



def drope_result(Devider_html,input_number)->list:
    drop=[]
    for x in range(input_number()):
        drop.append(Devider_html(get_page)[x])
    return drop


print(drope_result(Devider_html,input_number))

