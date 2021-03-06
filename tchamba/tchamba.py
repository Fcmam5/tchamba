# -*- coding: utf-8 -*-
import random
import requests
import string
from time import time
from datetime import datetime

# returns a randomly reordered version of the provided list
def randomize_list(list=[]):
    random.shuffle(list)
    return list

# returns a random timestamp
def random_timestamp():
    return random.randrange(int(time()))

# returns a random date since Jan 1st 1970
# optional date format may be passed
def random_date(format='%m-%d-%Y %H:%M:%S'):
    return datetime.fromtimestamp(random_timestamp()).strftime(format)

# returns a random string with a given length
# might return not beatiful results because it uses random_printable
def random_string_given_len(length)
    string_rand = ''
    for i in range(length)
        string_rand += random_printable()
    return string_rand

# returns a random string with a random length between the given min_length, max_length
# might return not beatiful results because it uses random_printable
def random_string_rand_len(min_length, max_length)
    string_rand = ''
    string_length = randint(min_length, max_length)
    for i in range(string_length)
        string_rand += random_printable()
    return string_rand

# returns a random char from the concatenation of ascii_lowercase and ascii_uppercase
def random_letter():
    return random.choice(string.ascii_letters)

# returns a random char from: 'abcdefghijklmnopqrstuvwxyz'
def random_lowercase():
    return random.choice(string.ascii_lowercase)

# returns a random char from: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def random_uppercase():
    return random.choice(string.ascii_uppercase)

# returns a random char from: '0123456789'
def random_digit():
    return random.choice(string.digits)

# returns a random char from: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
def random_punctuation():
    return random.choice(string.punctuation)

# returns a random char from the concatenation of digits, ascii_letters, punctuation, and whitespace.
def random_printable():
    return random.choice(string.printable)

def random_chuck_joke():
    try:
        data = requests.get("https://api.chucknorris.io/jokes/random").json()['value']
    except Exception:
        data = 'Chuck Norris doesn’t use web standards as the web will conform to him. AND YOU! CHECK YOUR INTERNET CONNECTION'

    return data

def random_hex_color():
    alpha = '0123456789abcdef'
    hex_color = '#'
    for i in range(6):
        hex_color += random.choice(alpha)
    return hex_color

def random_rgb_color():
    rgb_color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    return rgb_color

def random_pokemon():
    num = str(random.randint(1,700))
    data = requests.get('https://pokeapi.co/api/v2/pokemon/'+num).json()
    my_pokemon = data['forms'][0]['name']
    return my_pokemon

def random_fake_person():
    try:
        person =requests.get('http://api.namefake.com/random').json()
    except Exception:
        person = ""
    return person

def random_football_team():
    num = str(random.randint(1,890))
    try:
        football_team = requests.get('http://api.football-data.org/v1/teams/'+num).json()
    except Exception:
        football_team = ""
    return football_team

def random_word():
    try:
        word = requests.get("http://www.setgetgo.com/randomword/get.php").text
    except Exception as e:
        word = "potatoes"
    return word

def random_wikipedia_article():
    try:
        response = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&prop=revisions|extracts&exintro=&explaintext&rvprop=content").json()
        res = response['query']['pages'][response['query']['pages'].keys()[0]]

        article = {
            "title": res['title'],
            "text": res['extract']
        }

    except Exception as e:
        article = {
            "title": "Python",
            "text": "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale.\nPython supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.\nPython interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.\n\n"
        }
    return article

def random_yes_no_maybe():
    try:
        answer = requests.get("https://yesno.wtf/api").json()
    except Exception as e:
        answer = {
            "answer": "no",
            "forced": "true",
            "image": "https://yesno.wtf/assets/no/13-755222c98795431aa2e7d453ab1e75a1.gif"
        }
    return answer
