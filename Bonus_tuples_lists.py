#1. Accepts a list of movies, with each movie represented as a tuple containing the movie title, 
#release year, and a list of user ratings.
movies:list = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# Unpack the list
first_movie, second_movie, third_movie, forth_movie, fifht_movie, sixth_movie = movies

# Unpack the tuples
title1, release_year1, ratings1 = first_movie
title2, release_year2, ratings2 = second_movie
title3, release_year3, ratings3 = third_movie
title4, release_year4, ratings4 = forth_movie
title5, release_year5, ratings5 = fifht_movie
title6, release_year6, ratings6 = sixth_movie

#2. Calculates the average rating for each movie.
def average_rating (list) -> float:
    '''this function used to take a list of ratings and give the average of them'''
    total:int = 0
    average:float = 0.0
    for i in list:
        total += i
    average = round(total/len(list),2)
    return average

average_list:list = [
    average_rating(ratings1),
    average_rating(ratings2),
    average_rating(ratings3),
    average_rating(ratings4),
    average_rating(ratings5),
    average_rating(ratings6)
]
titles:list =[
    title1,
    title2,
    title3,
    title4,
    title5,
    title6
]
releases:list = [
    release_year1,
    release_year2,
    release_year3,
    release_year4,
    release_year5,
    release_year6
]

#4. Filters out movies with an average rating lower than 6.0 and display
def filter_and_display ():
    '''this function prints only movies with ratings higher than 6.0'''
    for i, rating in enumerate(average_list):
        #The enumerate() function in Python is used to iterate over a sequence 
        #(such as a list, tuple, or string) while keeping track of the index of the current item
        if rating >= 6:
            print(f"{i + 1}. {titles[i]} ({releases[i]}) - Average rating: {rating} ★")

filter_and_display()