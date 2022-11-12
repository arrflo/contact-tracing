#write a python program for contact tracing
#display menu of options
#1 - add an item 
#2 - search 
#3 - exit (y/n)

import sys

#print menu
print ("------ Menu ------\n \n 1 - add an item \n 2 - search \n 3 - exit (y/n) \n")
print ("------------------")
print ()

#ask user what to do
user__ = int(input ("What would you like to do? "))
dictionary = {
    "Fullname" : "  ",
    "Age" : "  ",
    "Address" : "  ",
    "Email" : "  ",
    "Phone Number" : "  "
}
#option1
if user__ == 1:
    dictionary["Fullname"] = input("Fullname: ")
    dictionary["Age"] = input("Age: ")
    dictionary["Address"] = input("Address: ")
    dictionary["Email"] = input("Email: ")
    dictionary["Phone Number"] = input("Phone Number: ")
    print("Saved!")
    #if proceeds to option #2
    cont = int(input ("What would you like to do? "))
    if cont == 2:
        ask = input("What would you like to search? (type 'all' for all data) ")
        if ask == "fullname" or ask == "Fullname":
            print ("Fullname: ", dictionary.get("Fullname"))
        elif ask == "age" or ask == "Age":
            print ("Age: ", dictionary.get("Age"))
        elif ask == "address" or ask == "Address":
            print ("Address: ", dictionary.get("Address"))
        elif ask == "email" or ask == "Email":
            print ("Email: ", dictionary.get("Email"))
        elif ask == "phone number" or ask == "Phone Number" or ask == "Phone Number":
            print ("Phone Number: ", dictionary.get("Phone Number"))
        elif ask == "all":
            print ("Fullname: ", dictionary.get("Fullname"))
            print ("Age: ", dictionary.get("Age"))
            print ("Address: ", dictionary.get("Address"))
            print ("Email: ", dictionary.get("Email"))
            print ("Phone Number: ", dictionary.get("Phone Number"))
    if cont == 3:
        a = input ("are you sure? (y/n)")
        if a == "y":
            sys.exit ()
if user__ == 3:
    a = input ("are you sure? (y/n)")
    if a == "y":
        sys.exit ()
    
# while True:
#     print menu
#     print ("------ Menu ------\n \n 1 - add an item \n 2 - search \n 3 - exit (y/n) \n")
#     print ("------------------")
#     print ()
#     ask user what to do
#     user__ = int(input ("What would you like to do? "))

#     empty dictionary
#     dictionary = {
#         "Fullname" : "  ",
#         "Age" : "  ",
#         "Address" : "  ",
#         "Email" : "  ",
#         "Phone Number" : "  "
#     }

    
#     if option 1 is chosen
#     if user__ == 1:
#         dictionary["Fullname"] = input("Fullname: ")
#         dictionary["Age"] = input("Age: ")
#         dictionary["Address"] = input("Address: ")
#         dictionary["Email"] = input("Email: ")
#         dictionary["Phone Number"] = input("Phone Number: ")
#         print ("Saved!")
#         user__ = int(input ("What would you like to do? "))
#         user proceeds to option 2
#         if user__ == 2:
#             user1__ = input ("What input would you like to search?(type 'all' for all data) ")
#             if user1__ == "fullname" or "Fullname":
#                 print ("Fullname: ", dictionary.get("Fullname"))
#             elif user1__ == "age" or "Age":
#                 print ("Age: ", dictionary.get("Age"))
#             elif user1__ == "address" or "Address":
#                 print ("Address: ", dictionary.get("Address"))
#             elif user1__ == "email" or "Email":
#                 print ("Email: ", dictionary.get("Email"))
#             elif user1__ == "phone number" or "Phone Number" or "Phone number":
#                 print ("Phone Number: ", dictionary.get("Phone Number"))
#             elif user1__ == "all":
#                 for key, value in dictionary.items():
#                     print (key, ":", value)
#         if user__ == 3:
#             a = input("are you sure? (y/n)")
#             if a == "y":
#                 break
    # if user__ == 2:
        # if user__ == 2:
        #     user1__ = input ("What input would you like to search?(type 'all' for all data) ")
        #     if user1__ == "fullname" or "Fullname":
        #         print ("Fullname: ",dictionary["Fullname"])
        #     elif user1__ == "age" or "Age":
        #         print ("Age: ",dictionary["Age"])
        #     elif user1__ == "address" or "Address":
        #         print ("Address: ",dictionary["Address"])
        #     elif user1__ == "email" or "Email":
        #         print ("Email: ",dictionary["Email"])
        #     elif user1__ == "phone number" or "Phone Number" or "Phone number":
        #         print ("Phone Number: ",dictionary["Phone Number"])
        #     elif user1__ == "all":
        #         for key, value in dictionary.items():
        #             print (key, ":", value)
    # if user__ == 3:
    #     a = input("are you sure? (y/n)")
    #     if a == "y":
    #         break




