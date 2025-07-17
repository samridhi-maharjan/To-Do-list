# To-Do List

A simple command-line To-Do List application in Python with persistent storage using a JSON file.

---

## Features

- Add new tasks
- View all tasks along with their status (Pending or Done)
- Mark tasks as completed(Done)
- Remove tasks

---
## Example commands and expected output

1. Add Task
2. View Task List
3. Mark Task Complete
4. Remove task
5. Exit app
Please select an option by entering its number: 1
Enter your task
Please enter one task at a time: Buy groceries
Task 'Buy groceries' added to the list.

## Clean code principles applied in the project
1. Single Responsibility Principle
    Each function has a single, well-defined responsibility:
    
    loadTasks(): Loads tasks from JSON file
    saveTasks(): Saves tasks to JSON file
    addTask(): Handles adding new tasks
    viewTask(): Displays task list
    completeTask(): Marks tasks as complete
    removeTask(): Removes tasks from list

2. Meaningful Names
    Functions and variables have descriptive names (addTask, viewTask, taskName)
    Constants and variables clearly indicate their purpose (tasks, searchTask)

3. Error Handling

Proper exception handling for file operations
Input validation for user choices
Graceful handling of invalid task numbers
Protection against empty task entries

4. Code Organization
    Logical separation of concerns
    Clear function structure
    Consistent indentation and formatting
    Proper use of global variables where necessary

5. User Experience
    Clear menu structure
    Informative error messages
    Confirmation messages for actions
    Input validation with helpful feedback

6. Data Persistence
    Automatic saving after each modification
    JSON format for human-readable storage
    Graceful handling of missing or corrupted data files
    
    Technical Details
    Data Structure
    Tasks are stored as a list of dictionaries:
    json[
        {
            "task": "Buy groceries",
            "Status": "Pending"
        },
        {
            "task": "Finish homework", 
            "Status": "Done"
        }
    ]
    Error Handling Examples
    Invalid menu choice:
    Please select an option by entering its number: 7
    Please enter number from 1 to 5!
    Non-numeric input:
    Please select an option by entering its number: abc
    Invalid input
    Empty task:
    Please enter one task at a time: 
    Task cannot be empty.
    Invalid task number:
    Enter the task number: 99
    Invalid Task Number
    Requirements

---

## Demo
<img width="701" height="680" alt="image" src="https://github.com/user-attachments/assets/326f726f-c29d-4d3d-b50e-a8bec23fe4f7" />
<img width="685" height="653" alt="image" src="https://github.com/user-attachments/assets/53632014-9c19-4d94-86f6-8ad4ad769978" />
<img width="512" height="437" alt="image" src="https://github.com/user-attachments/assets/d5d23228-731e-4837-8212-483bac497b83" />
<img width="661" height="560" alt="image" src="https://github.com/user-attachments/assets/47567d9d-0691-4e55-8b9e-5ef9a905bb6e" />





   
