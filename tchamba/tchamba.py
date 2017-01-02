# -*- coding: utf-8 -*-
import random
import requests
import string

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
