from literature_manag import *
from ratings_manage import *
import matplotlib.pyplot as plt

# A module is building a scatter plot, which helps to define in how many years the rating of the films based on books is higher than the number you choose
# RUN the program with entering a number in range 6 to 9
# The program will build a scatter plot with a horizontal line dividing the years where the average rating was lower than the given num and otherwise .It allows you to count the dots(it will be the number of years, when the average rating is the highest)


movies_ratings = read_file_ratings("ratings.list")  
rating_films = rating_of_films(movies_ratings)

years1 = []
years2 =[]
ratings1 = []
ratings2 = []


def dots_count_scatter(ratings):
    """
    The function expects as input a float or int number(the rating)
    you choose. The function depicts a scatter plot showing dependancies
    betweem the year the film was released and the rating it has
    """
    for year in rating_films.keys():
        if rating_films[year] > ratings:
            years1.append(year)
            ratings1.append(rating_films[year])
        else:
            years2.append(year)
            ratings2.append(rating_films[year])

    fig, ax = plt.subplots()
    ax.scatter(years1, ratings1, c="#e81405", s=25)
    ax.set_xlabel('Years', labelpad=20)
    ax.set_ylabel('Rating', labelpad=20)
    ax.scatter(years2, ratings2, c="#8205e8", s=25)
    ax.hlines(ratings, 1950, 2015)
    fig.suptitle("Dynamic of rating changes of films with years")
    plt.show()


if __name__ == "__main__":
    while True:
        try:
            rating = float(input("Enter the rating(from 6 to 9): "))
            if 6 <=rating <= 9:
                break
            else:
                raise Exception
        except:
            continue
    dots_count_scatter(rating)