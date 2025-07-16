import numpy as np

lists=[]
def main():
    print("TO-DO LIST")
    menu()

# menu function
def menu():
    while True:
        try:
            print("Welcome to the To-Do List app")
            print("Please select on of the operations")
            print("1. Add Task")
            print("2. View Task List")
            print("3. Mark Task Complete")
            print("4. Remove task")
            print("5. Exit app")
            
            choice=int(input("Press number of the desired operation"))     # get input from user
            # compare user's input with the operation index
            if choice==1:
                addTask()
            elif choice==2:
                viewTask()
            elif choice==3:
                completeTask()
            elif choice==4:
                removeTask()
            elif choice==5:
                closeApp()
                break
            else:
                print("Please enter number from 1 to 5")       #catches integer error
        except ValueError:
            print("invalid input")     #catches string error

def addTask():
    print("Enter your task")
    taskName=input("please enter one task at a time")
    print(taskName)
def viewTask():
    print("view")
def completeTask():
    print("complete")
def removeTask():
    print("remove")
def closeApp():
    print("quit")
if __name__ == "__main__":
    main()