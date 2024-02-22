# to do list program by Manuel Marchand
todo_list = []
def add_task(task):
    todo_list.append(str(task))
def view_tasks():
    for task in todo_list:
        print("TO DO LIST: ")
        print(task + "\n")

while True:
    user_input = input("What do you want to do, type 'add' to add a task, 'view' to view all tasks")
    if str(user_input) == "view":
        view_tasks()
    elif(str(user_input) == "add"):
        input_task = input("Type the task that you want to add to the list")
        add_task(input_task)