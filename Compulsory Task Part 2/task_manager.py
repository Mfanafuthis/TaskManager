"""This program works with two text files, user.txt and tasks.txt. tasks.txt
stores a list of all the tasks that the team is working on. user.txt stores the
username and password of each use that has permission to use the program."""

#=====importing libraries===========
import datetime #Import datetime library

#====Login Section====
"""The following loop request the user to enter password and user name until
the corret credintials"""
logins = True # Controlling variable
while logins:
    main_user_name = input("\nEnter user name: ")
    pass_word = input("Enter password: ")
    
    with open("user.txt", "r") as f:
        for line in f: 
            log_details = line.split(",") 
            """ Checks if the username and password match with existing in the
            file. Remove all the new line and space charectors before
            checking """
            if (main_user_name == log_details[0].strip()) \
               and (pass_word == log_details[1].strip()):
                # Print if the above true
                print("\nWelcome {}!!\n".format(main_user_name)) 
                logins = False # Update the controlling variable to false
                break
            
    if logins == True:
        print("\nPlease enter correct username or password!!")
        
    print("\n==============================================================\n")
                
while True:
    if(main_user_name == "admin") and (logins == False):
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - To view stats
e - Exit
: ''').lower()
        print("\n==============================================================\n")
    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
        print("\n==============================================================\n")
        
    if menu == 'r':
        if (main_user_name == "admin") and (logins == False):
            """ The following while loop checks if the user alread exist before
            registering"""
            exist = True
            while exist == True:
                exist = False
                user_name = input("Enter user name: ")
                with open("user.txt", "r+") as f:
                    for line in f:
                        log_details = line.split(",")
                        if (user_name == log_details[0].strip()):
                            exist = True
                            print("Username already exist!")
                            
            # The following loop verifies the password until they match
            verified = True
            while verified == True:
                pass_word = input("Enter password: ")
                ver_pass_word = input("Re-enter password: ")
                # Checks if the two passwords are the same
                if pass_word == ver_pass_word:
                    # Open a new object file f on an append mode
                    with open("user.txt", "a") as f:
                        # Adds username and password on to the text file
                        f.write("\n{}, {}".format(user_name,pass_word))
                        # Confirmation massage for the user
                        print("\nUsername and password added!") 
                        verified = False
                else:
                    print("\nPasswords do not match!")
        else:
            print("\nONLY ADMIN can register people!!")
            
        print("\n==========================================================\n")

    elif menu == 'a':
        """ The following loop request the user to enter a username of the
        person whom the task is to be assigned to. Request until the user has
        entered a correct username """
        username = True
        while username:
            user_name = input("Enter username of the person whom the task is \
assigned to: ")
            with open("user.txt", "r") as f:
                for line in f:
                    log_details = line.split(",")
                    if (user_name == log_details[0].strip()):
                        username = False
            if username == True:
                print("\nEnter correct username!!\n")
                
        task_title = input("Enter task title: ")
        task_discr = input("Enter task description: ")
        due_date = input("Enter due date (in DD/MM/YYYY): ")
        # Convert string due_date
        duedate = datetime.datetime.strptime(due_date,"%d/%m/%Y").date()  
        current_date = datetime.date.today()
        
        with open("tasks.txt","a") as f:
            # Writes all the details entered by user on file seperated by ","
            f.write("\n{}, {}, {}, {}, {}, No"\
                    .format(user_name,task_title,task_discr,
                            current_date.strftime("%d %b %Y"),
                            duedate.strftime("%d %b %Y"))) 
            print("\nTask addedd!!")    

        print("\n==========================================================\n")
            
    elif menu == 'va':
        # Displays all the tasks that are in the tasks.txt file
        with open("tasks.txt", "r") as f:
            for line in f:
                task_details = line.split(",")
                print(f"""\nTask:\t\t\t{task_details[1].strip()}
Assigned to:\t\t{task_details[0].strip()}
Date assigned:\t\t{task_details[3].strip()}
Due date:\t\t{task_details[4].strip()}
Task Complete?\t\t{task_details[5].strip()}
Task description:\t{task_details[2].strip()}\n""")
                
        print("\n==========================================================\n")
        
    elif menu == 'vm':
        """The following loop checks whether username entered exists and then
        displays all the tasks assigned to the user. Repeats until the correct
        username has been entered """
        found = True
        while found:
            with open("tasks.txt","r") as f:
                for line in f:
                    task_details = line.split(",")
                    if task_details[0] == main_user_name:
                        print(f"""\nTask:\t\t\t{task_details[1].strip()}
Assigned to:\t\t{task_details[0].strip()}
Date assigned:\t\t{task_details[3].strip()}
Due date:\t\t{task_details[4].strip()}
Task Complete?\t\t{task_details[5].strip()}
Task description:\t{task_details[2].strip()}\n""")
                        found = False
                        
            if (found == True):
                found = False
                print("\nThere are no tasks assigned to you!!")
                
        print("\n==========================================================\n")

    elif menu == 's':
        if main_user_name == "admin": # Checks if it's admin logged in
            user_list = []
            with open("user.txt","r") as f: # Create an object file f
                for line in f:
                    # Splits line where ever there is "," and store them as list
                    user_details = line.split(",")
                    # Adds the first item in the list to the user_list
                    user_list.append(user_details[0].strip()) 
                    
            for item in user_list:
                if item == "": # Checks for empty items in the list
                    user_list.remove(item) # Removes empty items
            # Print the lenght of the list        
            print("\nTotal number of users: {}".format(str(len(user_list)))) 
            
            task_list = []
            with open("tasks.txt","r") as f: # Create an object file f
                for line in f: 
                    task_details = line.split(",")
                    task_list.append(task_details[0].strip())
                    
            for item in task_list:
                if item == "":
                    task_list.remove(item)
                    
            print("Total number of tasks: {}\n".format(str(len(task_list))))
            
        print("\n==========================================================\n")
        
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
        print("\n==========================================================\n")
        
    else:
        print("You have made a wrong choice, Please Try again")
        print("\n==========================================================\n")

# Read on c-sharpcorner website about datetime libray
# https://www.c-sharpcorner.com/UploadFile/75a48f/working-with-date-and-time-python/


