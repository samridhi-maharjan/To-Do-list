def main():
    print("\t\tTO-DO LIST")
    print("\tWelcome to the To-Do List app")
    print("\n")
    while True:
        print("1. Add Task")
        print("2. View Task List")
        print("3. Mark Task Complete")
        print("4. Remove task")
        print("5. Exit app")
        
        choice=int(input("Please select an option by entering its number:"))     # get input from user
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
                print("Please enter number from 1 to 5!")       #catches integer error
        except ValueError:
            print("invalid input")     #catches string error

tasks=[]

# function to add new task
def addTask():
    print("Enter your task")
    taskName=input("Please enter one task at a time:")
    tasks.append({'task': taskName, 'Status':'Pending'})
    print(f"Task '{taskName}' added to the list.")
    print("\n")

#function to view t0-do list        
def viewTask():
    if len(tasks)==0:
        print("There are no pending tasks")
    else:
        print("\n")
        print("Task lists:")
        for index, task in enumerate(tasks,1):  #goes through tasks and index starts with 1
            print(f"{index}. {task['task']} - {task['Status']}")
    print("\n")

#funtion to mark task complete
def completeTask():
    if len(tasks)==0:
        print("List is Empty!\nAdd a Task")
    else:
        viewTask()
        try:
            searchTask=int(input("Enter the task number:"))-1
            if searchTask>=0 and searchTask<len(tasks):
                tasks[searchTask]['Status']='Done'
                print(f"Task {tasks[searchTask]['task']} has been completed.")
            else:
                print("Invalid Task Number")
            print("\n")
        except ValueError:
                print("Please enter a valid task number!")
        print("\n")

#function to remove task
def removeTask():
    if len(tasks)==0:
        print("List is Empty!\nAdd a Task")
    else:
        viewTask()
        try:
            searchTask=int(input("Enter the task number to delete:"))-1
            if searchTask>=0 and searchTask<len(tasks):
                removeTask=tasks.pop(searchTask)
                print(f"Task removed: {removeTask['task']}")
            else:
                print("Invalid Task Number")
            print("\n")
        except ValueError:
                print("Please enter a valid task number")
        print("\n")

#function to exit
def closeApp():
    print("quit")

main()