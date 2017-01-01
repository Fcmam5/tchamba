# Tchamba.random
Tchamba.random, is a real random data genarator (letters, jokes, names...)

## The idea
The name was invented by my friends Hammadi Ilyes and Bahri Aimene, and it was a joke. Now [we] are trying to implement it in order to get a random data.

## Installation
First install the **tchamba** package
```bash
  pip install tchamba
```

Then import it in your python file
```python
    from tchamba import *

    # Print a random character
    print random_char()

    # To print a random Chuck Norris joke (Internet connection needed)
    print random_chuck_joke()

    # Print a random hex color (ex: #02c65a)
    print random_hex_color()

    # Print a list of RGB color (ex: [31,12,15])
    print random_rgb_color()

    # Print a random Pokemon name
    print random_pokemon()

    # Get a fake person
    person = random_fake_person()
    for i in person:
        print i, person[i]
```

## Contributing
If you have an idea, please feel free to submit an issue, or fork this project and add your **awesome_random_function** in [tchamba.py](tchamba/tchamba.py) file.
I think that we need something cool, funny like this :smile: to use it in our programs, for testing or for fun.

## Credits
This package is using one of the bests APIs on the Web, like:
* [ChuckNorris.io](https://chucknorris.io)
* [PokeAPI](https://pokeapi.co)
* [NameFake](http://namefake.com/api)

## License
MIT licensed Done by Fortas Abdeldjalil and all [these awesome contributers](https://github.com/Fcmam5/tchamba/graphs/contributors).
