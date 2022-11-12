#write a python program for contact tracing
#display menu of options
#1 - add an item 
#2 - search 
#3 - exit (y/n)

while True:
    #print menu
    print ()
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
            a = input ("are you sure? (y/n) ")
            if a == "y":
                break
    #option2        
    if user__ == 2:
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
    #option3
    if user__ == 3:
        a = input ("are you sure? (y/n) ")
        if a == "y":
            break
    




