
![N|Solid](https://res.cloudinary.com/dzh5lsjmb/image/upload/v1541647602/large_films.ly.png)

[![Python 3.6+](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

[![PyPI version](https://badge.fury.io/py/filmsly.svg)](https://badge.fury.io/py/filmsly)

Do you love movies? Do you love using awesome apps like [Fandango](https://www.fandango.com/) and [AtomTickets](https://www.atomtickets.com/) for looking up showtimes? If yes, then you'll love this needlessly complicated way of finding that perfect showtime for Avengers 8.

### Features
* Finds theatre locations and information
* Finds movies and showtimes
* Automatically creates an offline indexing database during the first run, because successive scraping takes too long!
* Worried about theatre and movie name variations? Don't worry, every parameter is fuzzy matched for validation

### Installation

```sh
$ pip3 install filmsly --user
```
The `--user` is because the api class creates an indexing database to make your life easier

### Usage

```py
# Import filmsly.api class
from filmsly.api import filmsly_api

# Create filmsly object
filmsly_object = filmsly_api()

# Print a list parser mapped theatres
filmsly_object.list_of_theatres()

# Index a specific theatre
filmsly_object.index_theatre(theatre_name = 'HaRkIn') 

```

### Theatres Supported

Filmsly is currently capable of harvesting data from the following theatre chains.

| Theatre | Parser State |
| ------ | ------ |
| Harkins | PASSED |
| AMC | PASSED |
