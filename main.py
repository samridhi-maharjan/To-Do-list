import numpy as np

def main():
    print("\t\tTO-DO LIST")
    menu()
# menu function
def menu():
    while True:
        print("\tWelcome to the To-Do List app")
        print("\n")
        print("Please select on of the operations")
        print("1. Add Task")
        print("2. View Task List")
        print("3. Mark Task Complete")
        print("4. Remove task")
        print("5. Exit app")
        
        choice=int(input("Press number of the desired operation"))     # get input from user
        try:
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

tasks=[]
# function to add new task
def addTask():
    print("Enter your task")
    taskName=input("Please enter one task at a time")
    tasks.append({"task":taskName, "Status":"Pending"})
    print(f"Task '{taskName}' added to the list.")

#function to view t0-do list        
def viewTask():
    if len(tasks)==0:
        print("There are no pending tasks")
    else:
        print("Task lists:")
        for index, task in enumerate(tasks,1):  #goes through tasks and index starts with 1
            print(f"Task {index}. {task}")

def completeTask():
    print("complete")

def removeTask():
    print("delete")

def closeApp():
    print("quit")

main()