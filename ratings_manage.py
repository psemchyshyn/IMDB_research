import literature_manag
import csv


# Module for working with ratings list


movies,_ = literature_manag.read_file("literature.list")
films_and_years = literature_manag.movie_year(movies)
films = set([x[0] for x in films_and_years])
films_in_year = literature_manag.films_in_one_year(films_and_years)


def read_file_ratings(path):
    """
    A function for reading ratings.list IMDB database.
    A input it takes a path to file, and returns a list of tuples. Each tuple 
    is name of the movie and its rating
    """
    with open(path, "r", encoding="latin-1") as f:
        movies_ratings = []
        movies =set()
        for line in f:
            line = line.strip()
            if "\"" in line:
                line = line.split("\"")
                rating = line[0][len(line[0]) - 6: len(line[0])].strip()
                if line[1] in films:
                    if line[1] not in movies and rating != "":
                        movies_ratings.append((line[1], float(rating)))
                        movies.add(line[1])
    return movies_ratings


movies_ratings = read_file_ratings("ratings.list")  


# Writing to csv
def top100_films_to_csv(path, movies_ratings, num):
    """
    A function for writing films with top ratings to csv file.
    As input the function takes a path to file, movie_ratings(
    a list of tuples of movies and its ratings), and a number of films you want
    write in.
    """
    arr = []
    movies = [x[0] for x in movies_ratings]
    ratings = [x[1] for x in movies_ratings]
    for element in range(num):
        max_rating_pos = ratings.index(max(ratings))
        if movies[max_rating_pos] in films:
            arr.append([movies[max_rating_pos], max(ratings)])
            movies.remove(movies[max_rating_pos])
            ratings.remove(max(ratings))
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(arr)


def rating_of_films(movies_ratings, films_in_year=films_in_year):
    """
    A function for finding the average rating of films in each year.
    As input it takes movies_ratings and films in the year and returns a dictionary
    with a movie name in as the key and its rating as a value.
    """
    year_rat_dict = {}
    for year in range(1950, 2010):
        year_rat_dict[year] =  set()
        for film_rat in movies_ratings:
            if film_rat[0] in films_in_year[year]:
                year_rat_dict[year].add(film_rat[1]) 
                movies_ratings.remove(film_rat)
    for i in year_rat_dict:
        year_rat_dict[i] = round(sum(x for x in year_rat_dict[i])/len(list(year_rat_dict[i])),2)
    return year_rat_dict


def top_films_in_year(rating_films, num=5):
    """
    A function for finding top n years with the highest
    rating on IMDB. It takes as input rating_films value 
    and returns a list of tuples of years with the
    highest rating
    """
    rating_films = {y: x for x, y in rating_films.items()}
    top_films = []
    for i in range(num):
        key = max(list(rating_films.keys()))
        top_films.append((rating_films[key], key))
        rating_films.pop(key)
    return top_films


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    top100_films_to_csv("top100_films_.csv", movies_ratings, 100)

    year_rat_dict = rating_of_films(movies_ratings)
    top_films = top_films_in_year(year_rat_dict)
    print(year_rat_dict)

          


    
