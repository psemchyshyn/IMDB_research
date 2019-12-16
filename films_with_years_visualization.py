from literature_manag import *
import matplotlib.pyplot as plt


# Module for visualisation of data (dependancies between the amount of films and the years they were released)
# RUN the module to garner a bar and a scatter plot of given data


films, books = read_file("literature.list") 
movie_with_year = movie_year(films)  #extracting movie and year
data = amount_of_films_per_year(movie_with_year)
years = list(data.keys())
film_amount = list(data.values())


def films_years_histogram(years=years, film_amount= film_amount):
    """
    As input a function takes list of years and list of the number of movies
    thay were shot in these years. It returns a histogram which depicts
    this dependancy
    """
    fig, axs = plt.subplots()
    axs.bar(years, film_amount, color="#fc0303")
    fig.suptitle('Dynamic of production of films based on books')
    plt.show()


if __name__ == "__main__":
    films_years_histogram()