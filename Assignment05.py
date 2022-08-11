# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# HGaylord,8.11.22,Finished Script
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
lstRow=[]


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
myfile=open("ToDoList.txt", 'a+')
for row in myfile:
    lstRow=row.split(",")
    dicRow={'Task': lstRow[0].strip(), 'Priority': lstRow[1].strip()}
    lstTable.append(dicRow)
myfile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)


    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print ("Your Current Data is:" "\n" )
        for row in lstTable:
            print(row['Task']+','+row['Priority'])
        continue





    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        stringTask=input(str(("Please add a task" "\n")))
        stringPriority=input(str(("Please give this task a priority" "\n")))
        dicRow={'Task':stringTask, 'Priority':stringPriority}
        lstTable.append(dicRow)
        continue





    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        lstTable.pop()
        print("Last Item Removed!""\n")
        print("Current to do list: " , lstTable)
        continue





    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        myfile=open(objFile,"w+")
        for row in lstTable:
            myfile.write(row["Task"] + "," + row["Priority"] + "\n")
        myfile.close()
        print("Thanks, your file has been saved.")
        continue





    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("If you are sure you want to quit and not save your entries, please press enter")
        break  # and Exit the program
