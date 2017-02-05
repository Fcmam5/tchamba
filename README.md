# Tchamba.random [![Build Status](https://travis-ci.org/Fcmam5/tchamba.svg?branch=master)](https://travis-ci.org/Fcmam5/tchamba)
Tchamba.random, is a real random data genarator (letters, jokes, names...)

## The idea
The name was invented by my friends Hammadi Ilyes and Bahri Aimene, and it was a joke. Now [we] are trying to implement it in order to get random data.

## Installation
First install the **tchamba** package
```bash
  pip install tchamba
```
## How to use
Import **tchamba** in your python file and use any of the functions :
```python
    from tchamba import *

    # Print a random letter (Uppercase and undercase letters included)
    print random_letter()

    # Print a random lowercase letter
    print random_lowercase()

    # Print a random uppercase letter
    print random_uppercase()

    # Print a random digit
    print random_digit()

    # Print a random punctuation mark ( includes these chars !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~  )
    print random_punctuation()

    # Print a random printable char from the concatenation of digits, ascii_letters, punctuation, and whitespaces.
    # [might return crazy characters like a Carriage Return, a Vertical Tabulator, or a Form Feed]
    print random_printable()

    # Print a random string with a given length
    # might return ugly results because it uses random_printable
    print random_string_given_len(42)

    # Print a random string with a random length between the given min_length and max_length
    # might return ugly results because it uses random_printable
    print random_string_rand_len(1, 20)

    # To print a random Chuck Norris joke (Internet connection needed)
    print random_chuck_joke()

    # Print a random hex color (ex: #02c65a)
    print random_hex_color()

    # Print a list of RGB color (ex: [31,12,15])
    print random_rgb_color()

    # Print a random Pokemon name (Internet connection needed)
    print random_pokemon()

    # Get a fake person (Internet connection needed)
    person = random_fake_person()
    for i in person:
        print i, person[i]

    # Get a random football team (Internet connection needed)
    football_team = random_football_team()

    # Print a random word (Internet connection needed) or it returns 'potatoes'
    print random_word()

    # Get and print random Wikipedia article (Internet connection needed) or it will return "Python article"
    article = random_wikipedia_article()
    print article['title']
    print article['text']
```

## Contributing
If you have an idea, please feel free to submit an issue, or fork this project and add your **awesome_random_function** in [tchamba.py](tchamba/tchamba.py) file.
I think that we need something cool and funny like this :smile: to use in our programs, for testing or for fun.

## Credits
This package is using some of the best APIs on the Web, like:
* [ChuckNorris.io](https://chucknorris.io)
* [PokeAPI](https://pokeapi.co)
* [NameFake](http://namefake.com/api)
* [Football Teams api](http://api.football-data.org)

## License
MIT licensed Done by Fortas Abdeldjalil and all [these awesome contributers](https://github.com/Fcmam5/tchamba/graphs/contributors).
