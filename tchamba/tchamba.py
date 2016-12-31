# -*- coding: utf-8 -*-
import random
import requests
import string

def random_char():
    return random.choice(string.letters)

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
