#James D. Ellis 2/28/2018

media_type = input("which do you prefer movies or books?: ")

if media_type == "movies":
 input("what is the name of the movie you choose: ")
 

else:
    input("what is the name of the book you choose: ")



Genre_ = input("what genre is this book/movie?: ")

rating_ = float(input ("what is your rating of this book/movie on a scale of 1-10: "))

describe_ = input("give a brief description of your book/movie: ")

new_list = []

new_list.append(media_type )  

new_list.append(Genre_)

new_list.append(rating_)

new_list.append(describe_)



print (new_list)

if rating_ in range(1,3):
 print ("you think poorly of this movie.")

elif rating_ in  range(4,6):
 print("this movie is average.")

else:
 print ("this movie is above average.") 



