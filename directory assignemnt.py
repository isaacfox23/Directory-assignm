# I really struggled with this project too:( Getting the user input and integrating it was pretty simple but I feel like we really didn't go over a lot of the directory stuff that well. I ended up using the youtube videos I searched and linked below, materials in class,programiz  and the book to help me look for the user directory and create one if it wasn't there but it was a definite struggle!

#I tried my best just taking little pieces from here and there!
#https://www.youtube.com/watch?v=Uh2ebFW8OYM
#https://www.youtube.com/watch?v=E1gDJU9Q4kg
#https://www.youtube.com/watch?v=vNP15Wov7sQ
#https://www.youtube.com/watch?v=DvZTW5g82pQ
#https://www.programiz.com/python-programming/directory, took. a lot of stuff from this one including some of the comments on the actual youtube vid itself.
import os

#gathering user info and storing them as strings obviously, we do not need to mess with any of the other forms of data for this project except strings
user_direct = input("What directory do you want to store the file in?")
user_file= input("What would you like your file name to be? ")
user_name= input("what is your full name? ")
user_address = input("What is your full address? ")
user_number = input("What is your phone number?  ")

#lets try and look for user directory using if statement to help me and create new too.This is really the part of the project where I struggled the most trying to piece things together from all the sources but I feel like I have a good framework at least!
if os.path.isdir(user_direct):
  new_file = open(os.path.join(user_direct, user_file), "w")
  new_file.write(user_name + user_address + user_number)
  # gotta make sure to close your files after
  new_file.close()
  print("the contents of this file are:")
  new_file = open(os.path.join(user_direct, user_file), "r")
  #trying to display the contents to the user as program output through the read command!
  print(new_file.read())
  # gotta make sure to close your files after
  new_file.close()
