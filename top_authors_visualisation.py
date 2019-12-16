import matplotlib.pyplot as plt 
from literature_manag import *


# Module for visualisation of data
# A program asks user to enter the number n of authors and will create a bar with n authors, on whose works there was the biggest amount of films shot.


films, books = read_file("literature.list") 
bokauth = book_author(books)  #extracting movie and year
data = amount_of_author_books(bokauth)


def top_author_histogram(authors, amount_of_books):
       """
       A function takes as input a list of ten authors, which has 
       the biggest amount of their books released in film industry
       and a list of the number of that list. The function 
       returns a histogram portraying those dependancies
       """
       fug, ax = plt.subplots()
       ax.barh(authors, amount_of_books, align='center')
       ax.invert_yaxis()  # labels read top-to-bottom
       ax.set_xlabel('Amount of books', labelpad=20)
       ax.set_ylabel('Authors')
       ax.set_title(f'Statistics of top {number} authors, whose books were used in kinomatography')
       plt.show()


if __name__ == "__main__":
       while True:
        try:
            number = int(input("Enter the number of authors(no more than 30): "))
            if 1 <= number <= 30:
                break
            else:
                raise Exception
        except:
            continue
       top_authors = top_ten_authors(data, number)
       authors = [x[0] for x in top_authors]
       amount_of_books = [y[1] for y in top_authors]
       top_author_histogram(authors, amount_of_books)

