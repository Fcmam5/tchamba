# Tchamba.random
Tchamba.random, is a real random data genarator (letters, jokes, names...)

## The idea
The name was invented by my friends Hammadi Ilyes and Bahri Aimene, and it was a joke. Now [we] are trying to implement it in order to get a random data.

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

    # Get a random word (Internet connection needed) or it returns 'potatoes'
    print random_word()

    # Get a random Wikipedia article (Internet connection needed) or it will return "Python article"
    article = random_wikipedia_article()
    print article['title']
    print article['text']
```

## Contributing
If you have an idea, please feel free to submit an issue, or fork this project and add your **awesome_random_function** in [tchamba.py](tchamba/tchamba.py) file.
I think that we need something cool, funny like this :smile: to use it in our programs, for testing or for fun.

## Credits
This package is using one of the bests APIs on the Web, like:
* [ChuckNorris.io](https://chucknorris.io)
* [PokeAPI](https://pokeapi.co)
* [NameFake](http://namefake.com/api)
* [football teams api](http://api.football-data.org)

## License
MIT licensed Done by Fortas Abdeldjalil and all [these awesome contributers](https://github.com/Fcmam5/tchamba/graphs/contributors).
