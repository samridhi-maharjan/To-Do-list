tasks=[]
# if _name_ == '_main_':

# main function
def main():
    print("TO-DO LIST")
    menu()

# menu function
def menu():
    while True:
        try:
            print("Welcome to the To-Do List app")
            print("Please select on of the operations")
            print("1. Add task")
            print("2. View Task List")
            print("3. Mark Task Complete")
            print("4. Remove task")
            print("5. Exit app")
            
            choice=int(input())     # get input from user
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
                print("error")
        except ValueError:
            print("invalid input")

def addTask():
    print("add")
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