#write a python program for contact tracing
#display menu of options
#1 - add an item 
#2 - search 
#3 - exit (y/n)

import sys

#print menu
print ()
print ("------ Menu ------\n \n 1 - add an item \n 2 - search \n 3 - exit (y/n) \n")
print ("------------------")
print ()

#ask user what to do
while True:
    user__ = int(input ("What would you like to do? "))
    #full name as key, value as dictionary
    #existing contact tracing infos:
    dictionary = {
        "LISA": {"Age":"25","Address":"SK", "Email":"blackpinklisa@gmail.com","Phone Number":"XXX"},
        "JENNIE": {"Age":"26","Address":"SK", "Email":"blackpinkjennie@gmail.com","Phone Number":"XXX"},
        "ROSIE": {"Age":"25","Address":"SK", "Email":"blackpinkrosie@gmail.com","Phone Number":"XXX"},
        "JISOO": {"Age":"27","Address":"SK", "Email":"blackpinkjisoo@gmail.com","Phone Number":"XXX"}
    }
    #option1
    if user__ == 1:
        fullname = input("Fullname: ")
        info = {
            fullname:{
                "Age":input("Age: "),
                "Address": input("Address: "),
                "Email": input ("Email: "),
                "Phone Number": input("Phone Number: ")
            }
        }
        print("Saved!")
        dictionary.update(info)
        #insert print code
        ques = input("Would you like to add another one?(y/n) ")
        while ques == "y":
            fullname = input("Fullname: ")
            info = {
                fullname:{
                    "Age":input("Age: "),
                    "Address": input("Address: "),
                    "Email": input ("Email: "),
                    "Phone Number": input("Phone Number: ")
                }
            }
            print("Saved!")
            dictionary.update(info)
            ques = input("Would you like to add another one?(y/n) ")
        #proceeds to 2
        while True:
            user1__ = int(input ("What would you like to do? "))
            if user1__ == 1:
                print ("I thought you don't have anything to add anymore? ")
                print ("Well then, okay!")
                fullname = input("Fullname: ")
                info = {
                    fullname:{
                        "Age":input("Age: "),
                        "Address": input("Address: "),
                        "Email": input ("Email: "),
                        "Phone Number": input("Phone Number: ")
                    }
                }
                print("Saved!")
                dictionary.update(info)
                ques = input("Would you like to add another one?(y/n) ")
                while ques == "y":
                    fullname = input("Fullname: ")
                    info = {
                        fullname:{
                            "Age":input("Age: "),
                            "Address": input("Address: "),
                            "Email": input ("Email: "),
                            "Phone Number": input("Phone Number: ")
                        }
                    }
                    print("Saved!")
                    dictionary.update(info)
                    ques = input("Would you like to add another one?(y/n) ")
            if user1__ == 2:
                search = input("Who would you like to search? (Enter their full name) ")
                if search in dictionary.keys():
                    find = dictionary[search]
                    print(search)
                    print ("Age: ", find.get("Age"))
                    print ("Address: ", find.get("Address"))
                    print ("Email: ", find.get("Email"))
                    print ("Phone Number: ", find.get("Phone Number"))
                else:
                    print("It seems like the info you're looking for does not exist in our records.")
            if user1__ == 3:
                ask = input("are you sure?(y/n) ")
                if ask == "y":
                    sys.exit()
    #option 2
    if user__ == 2:
        search = input("Who would you like to search? (Enter their full name) ")
        if search in dictionary.keys():
            find = dictionary[search]
            print(search)
            print ("Age: ", find.get("Age"))
            print ("Address: ", find.get("Address"))
            print ("Email: ", find.get("Email"))
            print ("Phone Number: ", find.get("Phone Number"))
        else:
            print("It seems like the info you're looking for does not exist in our records.")
    #option 3
    if user__ == 3:
        ask = input("are you sure? (y/n) ")
        if ask == "y":
            break
            

