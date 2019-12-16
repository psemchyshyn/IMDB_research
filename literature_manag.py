from typing import List, Tuple, Union, Callable, Dict
import csv

# The module is for working with literature list.


# Reading file
def read_file(path: str) -> Tuple[List[str], List[str]]:
    """
    A function for reading the 
    file with movies list, which are based on books,
    As input the function takes a path
    to file and returns a tuple, which consists of
    two lists - the first one contains 
    lines with movies and the year they were released
    and the second has the information 
    about the book, on which this film was based on.
    """
    with open(path, "r", encoding="latin-1") as f:
        lit_list = []
        movies_list = []
        have_lit = False
        for line in f:
            if line.startswith("MOVI"):
                movies_list.append(line)
                have_lit = False
            if (line.startswith("BOOK") or line.startswith("NOVL") or line.startswith("ADPT")) and not have_lit and "\"" in line:
                lit_list.append(line)
                have_lit = True     
    return movies_list, lit_list


# Working with films
def movies_fox_decorator(movie_year):
    """
    Decorator for the movie_year function,
    which prints the resulted output of this
    function
    """
    def wrapper(list_of_movies):
        film_year = movie_year(list_of_movies)
        for i in  film_year:
            print(i)
        return film_year
    return wrapper


#@movies_fox_decorator
def movie_year(list_of_movies: List[str]) -> List[tuple]:
    """
    A function takes a list of strings
    (this list is a first element of a tuple,
    that read_file function returns) and returns
    a list, which consists of tuples of name of the film
    and the year it was released
    """
    data = list_of_movies
    film_and_year = []
    films = set()
    for line in data:
        first_par = line.find("(")
        year = line[first_par + 1: first_par +5].strip()
        if not year.isdigit(): year = 2016
        else: year = int(year)
        lower_boundary = line.find(":")
        film_name = line[lower_boundary + 1: first_par].strip().replace("\"", "")
        if film_name not in films:
            films.add(film_name)
            film_and_year.append((film_name, year))
    return film_and_year


def films_in_one_year(film_and_year: List[tuple]) -> Dict[int, set]:
    """
    A function, which takes a list, which consists
    of name of film and the year of release(the input
    is given from the function movie_year) and returns
    a dictionary with the years of release as the key and
    a set of movies as the value
    """
    dict_of_years = {}
    for element in film_and_year:
        if element[1] not in dict_of_years:
            dict_of_years[element[1]] = set()
            dict_of_years[element[1]].add(element[0])
        else:
            dict_of_years[element[1]].add(element[0])
    return dict_of_years


def amount_of_films_per_year(film_and_year: List[tuple]) -> Dict[int, int]:
    """
    A function, which takes a list, which consists
    of name of film and the year of release(the input
    is given from the function movie_year) and returns
    a dictionary with the years of release as the key and a number 
    of films, which were released in this time
    """
    dict_of_years = {}
    for element in film_and_year:
        if element[1] not in dict_of_years:
            dict_of_years[element[1]] = 1
        else:
            dict_of_years[element[1]] += 1
    return dict_of_years


# Working with writers and books
def book_author(list_of_books: List[str]) -> List[tuple]:
    """
    A function takes a list of strings
    (this list is a second element of a tuple,
    that read_file function returns) and returns
    a list of tuples that contain name of the book 
    and the name of the author by whom it was written
    """
    data = list_of_books
    book_and_author = []
    for line in data:
        lower_boundary = line.find(":")
        upper_boundary = line.find(".")
        author = line[lower_boundary + 1: upper_boundary].strip()
        book_name = line.split("\"")[1]
        book_and_author.append((book_name, author))
    return book_and_author


def books_of_author(books_and_author: List[tuple]) -> Dict[str, str]:
    """
    A function which takes a list of tuples with the name
    of the book and the author that wrote it. The
    function returns a dictionary with the author as the key and books that he 
    wrote as a value(in form of set)
    """
    dict_of_books = {}
    for element in books_and_author:
        if element[1] not in dict_of_books:
            dict_of_books[element[1]] = set()
            dict_of_books[element[1]].add(element[0])
        else:
            dict_of_books[element[1]].add(element[0])
    return dict_of_books


def amount_of_author_books(books_and_author: List[tuple]) -> Dict[str, int]:
    """
    A function which takes a list of tuples with the name
    of the book and the author that wrote it. A function return 
    a dictionary with the author name as the key and with the value
    of integer - number of books he/she wrote for the film production
    """
    dict_of_books = {}
    for element in books_and_author:
        if element[1] not in dict_of_books:
            dict_of_books[element[1]] = 1
        else:
            dict_of_books[element[1]] += 1
    return dict_of_books


def top_ten_authors(dict_of_books: Dict[str, int], n: int) -> List[str]:
    """
    A function takes as input a dictionary of author as key,
    and the amounts of his books, that were included in films 
    as value + numbers of authors you want to see. It returns a list of authors, which has the 
    biggest amount of books in film industry 
    """
    top_authors = []
    dict_of_books = {y:x for x,y in dict_of_books.items()}
    for i in range(n):
        key = max(dict_of_books.keys())
        top_authors.append((dict_of_books[key], key))
        dict_of_books.pop(key)
    return top_authors


# Linking films and the books
def film_book(film_and_year, book_and_author):
    films = [x[0] for x in film_and_year]
    authors = [y[1] for y in book_and_author]
    print(len(films), len(authors))
    return [(film, author) for film, author in zip(films, authors)]


# Calling functions, printing the results
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    movies, books = read_file("literature.list")
    book_and_authors = book_author(books)
    film_and_years = movie_year(movies)
    dict_of_years = films_in_one_year(film_and_years)
    amount_in_one_year = amount_of_films_per_year(film_and_years)
    dict_of_books = amount_of_author_books(book_and_authors)
    top_authors = top_ten_authors(dict_of_books, 10)
    print(top_authors)
    # Here is available values to print
    # Check in documentation for what the function returns, then print the value!
  

    




        



         