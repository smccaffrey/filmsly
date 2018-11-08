
![N|Solid](https://res.cloudinary.com/dzh5lsjmb/image/upload/v1541647602/large_films.ly.png)

Do you love movies? Do you love using awesome apps like Fandango and atomtickets for looking up showtimes? If yes, then you'll love this complicated way of finding that perfect showtime for Avengers 8.

### Installation

```sh
$ pip install filmsly
$
$ from filmsly.api import filmsly_api
$
$ _test = filmsly_api()
$ print(_test.list_of_theatres())
$ re = _test.get_theatres()
```

### Theatres Supported

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Theatre | Parser Status |
| ------ | ------ |
| Harkins | PASSED |
| AMC | PASSED |
|   |   |
|   |   |