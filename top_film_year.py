from literature_manag import *
from ratings_manage import *
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import copy

# Module for building a scatter plot based on given data
# The program asks to enter the number n(it will be the amount of years)
# The resulted plot will portray top years and rating, where the average ratings of the films based on books were the highest


movies_ratings = read_file_ratings("ratings.list")  
rating_films = rating_of_films(movies_ratings)


def top_visualization(num):
    """
    The function for building a graphic.
    As input it takes the number of years and
    it builds a scatter plot where the average 
    ratings of the films based on books were the highest
    """
    top_year_films = top_films_in_year(rating_films, num)
    print(top_year_films)
    years = [x[0] for x in top_year_films]
    top_ratings = [x[1] for x in top_year_films]
    tops = copy.deepcopy(top_ratings)
    rng = np.random.RandomState(0)
    colors = rng.rand(len(years))
    sizes = []
    for i in range(1, len(years) + 1):
        n = max(tops)
        sizes.append(100*i)
        tops.remove(n)

    plt.scatter(years, top_ratings, c=colors, s=list(reversed(sizes)), alpha=0.6,
                cmap='viridis')
    plt.xlabel("Years", labelpad=15)
    plt.ylabel("Ratings", labelpad=18)
    plt.colorbar(); 
    plt.show()


if __name__ == "__main__":
    while True:
        try:
            number = int(input("How many years with top film ratings do you want to see?(no more than 30): "))
            if 1 <= number <= 30:
                break
            else:
                raise Exception
        except:
            continue
    top_visualization(number)


