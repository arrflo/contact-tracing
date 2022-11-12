#write a python program for contact tracing
#display menu of options
#1 - add an item 
#2 - search 
#3 - exit (y/n)

#print menu
print ("------ Menu ------\n \n 1 - add an item \n 2 - search \n 3 - exit (y/n) \n")
print ("------------------")
print ()
#ask user what to do
user__ = int(input ("What would you like to do? "))
#empty dictionary
dictionary = {
    "Fullname" : "  ",
    "Age" : "  ",
    "Address" : "  ",
    "Email" : "  ",
    "Phone Number" : "  "
}


