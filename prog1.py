#write a python program for contact tracing
#display menu of options
#1 - add an item 
#2 - search 
#3 - exit (y/n)

#printmenu
print ("------ Menu ------\n \n 1 - add an item \n 2 - search \n 3 - exit (y/n) \n")
print ("------------------")
print ()
#ask user what to do
user__ = int(input ("What would you like to do? "))
#create a dictionary that stores info
dict1 = {
    "Fullname" : input ("Fullname: "),
    "Age" : input ("Age: "),
    "Address" : input("Address: "),
    "Email" : input ("Email: "),
    "Phone Number" : input ("Phone Number: ")
}
#

