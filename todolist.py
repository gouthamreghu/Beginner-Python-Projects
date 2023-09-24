#creation

def create_task(task):
    with open('tasks.txt','a') as file:
        file.write(task + '\n')

#Tracking

def track_tasks():
    with open('tasks.txt','r') as file:
        tasks = file.readlines()
    if tasks:
        for i,task in enumerate(tasks, start=1):
            print(f"(i). {task.strip()}")
        else:
            print("No tasks found")

#update

def update_task(task_number, updated_task):
    with open('tasks.txt','r') as file:
        tasks = file.readlines()
    if task_number <= len(tasks):
        tasks[task_number - 1] = updated_task + '\n'
        with open('tasks.txt','w') as file:
            file.writelines(tasks)
        print("Task Updated Succesfully!")
    else:
        print("Invalid task number.Task not updated!")

while True:
    print("\nCommand Menu:")
    print("1. Create a task")
    print("2. Track tasks")
    print("3. Update a task")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == '1':
        task = input("Enter the task: ")
        create_task(task)
    elif choice == '2':
        track_tasks()
    elif choice == '3':
        task_number = int(input("Enter the task number to update: "))
        updated_task = input("Enter the updated task: ")
        update_task(task_number, updated_task)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose a valid option.")



