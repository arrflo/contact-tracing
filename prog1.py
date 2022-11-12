#write a python program for contact tracing
#display menu of options
#1 - add an item 
#2 - search 
#3 - exit (y/n)
while True:
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
    #if option 1 is chosen
    if user__ == 1:
        dictionary["Fullname"] = input("Fullname: ")
        dictionary["Age"] = input("Age: ")
        dictionary["Address"] = input("Address: ")
        dictionary["Email"] = input("Email: ")
        dictionary["Phone Number"] = input("Phone Number: ")
        print ("Saved!")
        user__ = int(input ("What would you like to do? "))
        #user proceeds to option 2
        if user__ == 2:
            user1__ = int(input ("What input would you like to search?(type 'all' for all data) "))
            if user__ == "fullname" or "Fullname":
                print ("Fullname: ",dictionary["Fullname"])
            elif user__ == "age" or "Age":
                print ("Age: ",dictionary["Age"])
            elif user__ == "address" or "Address":
                print ("Address: ",dictionary["Address"])
            elif user__ == "email" or "Email":
                print ("Email: ",dictionary["Email"])
            elif user__ == "phone number" or "Phone Number" or "Phone number":
                print ("Phone Number: ",dictionary["Phone Number"])
            elif user__ == "all":
                for key, value in dictionary.items():
                    print (key, ":", value)
        #clears the list
        if user__ == 3:
            break
    if user__ == 2:
        if user__ == 2:
            user1__ = int(input ("What input would you like to search?(type 'all' for all data) "))
            if user__ == "fullname" or "Fullname":
                print ("Fullname: ",dictionary["Fullname"])
            elif user__ == "age" or "Age":
                print ("Age: ",dictionary["Age"])
            elif user__ == "address" or "Address":
                print ("Address: ",dictionary["Address"])
            elif user__ == "email" or "Email":
                print ("Email: ",dictionary["Email"])
            elif user__ == "phone number" or "Phone Number" or "Phone number":
                print ("Phone Number: ",dictionary["Phone Number"])
            elif user__ == "all":
                for key, value in dictionary.items():
                    print (key, ":", value)
    if user__ == 3
        break




