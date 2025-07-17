import json
import os

tasks = []

def loadTasks():
    #loads tasks from the JSON file at start
    global tasks
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                tasks = json.load(f)
        except Exception as e:
            print(f"Could not read tasks.json: {e}")
            tasks = []

def saveTasks():
    #save current tasks to the JSON file.
    try:
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"Failed to save tasks: {e}")
def main():
    loadTasks()
    print("\t\tTO-DO LIST")
    print("\tWelcome to the To-Do List app")
    print("\n")
    while True:
        print("1. Add Task")
        print("2. View Task List")
        print("3. Mark Task Complete")
        print("4. Remove task")
        print("5. Exit app")
        
        try:
            choice=int(input("Please select an option by entering its number:"))
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
            print("invalid input")                              #catches string error

#function to add new task
def addTask():
    print("Enter your task")
    taskName=input("Please enter one task at a time:")
    tasks.append({'task': taskName, 'Status':'Pending'})
    saveTasks()
    print(f"Task '{taskName}' added to the list.")
    print("\n")
#function to view tasklist        
def viewTask():
    if len(tasks)==0:
        print("There are no pending tasks")
    else:
        print("\n")
        print("Task lists:")
        for index, task in enumerate(tasks,1):              #loops through the tasks list with an index starting at 1 for user-friendly numbering
            print(f"{index}. {task['task']} - {task['Status']}")
    print("\n")
#function to mark task complete
def completeTask():
    if len(tasks)==0:
        print("List is Empty!\nAdd a Task")
    else:
        viewTask()
        try:
            searchTask=int(input("Enter the task number:"))-1
            if searchTask>=0 and searchTask<len(tasks):
                tasks[searchTask]['Status']='Done'          #mark the selected task as completed
                saveTasks()
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
                deleteTask=tasks.pop(searchTask)
                print(f"Task removed: {deleteTask['task']}")
            else:
                print("Invalid Task Number")
            print("\n")
        except ValueError:
                print("Please enter a valid task number")
        print("\n")
#function to exit
def closeApp():
    print("Thank you for using the app")

if __name__ == "__main__":
    main()