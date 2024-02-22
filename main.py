# to do list program by Manuel Marchand
todo_list = []
def add_task(task):
    todo_list.append(str(task))
def view_tasks():
    print("TO DO LIST: ")
    for i, task in enumerate(todo_list):
        print(str(i+1) + ") " + task)

def mark_task(index_num):
    if "(Completed)" not in todo_list[index_num]:
        todo_list[index_num] = todo_list[index_num] + " (Completed)"

def delete_task(index_num):
    if (index_num < len(todo_list)) and (index_num > -1):
        del todo_list[index_num]

while True:
    user_input = input("What do you want to do, type 'add' to add a task, 'view' to view all tasks, 'mark' to mark one as completed, or 'save' to save to a file: ")
    if str(user_input) == "view":
        view_tasks()
    elif(str(user_input) == "add"):
        input_task = input("Type the task that you want to add to the list: ")
        add_task(input_task)
    elif(str(user_input) == "mark"):
        user_input = input("Type the number of the task that you want to mark as completed: ")
        mark_task(int(user_input)-1)
    elif(str(user_input) == "delete"):
        user_input = input("Type the number of the task that you want to delete: ")
        delete_task(int(user_input)-1)
    elif(str(user_input) == "save"):
        file = open("output.txt", "a")
        file.truncate(0)
        file.write("TO DO LIST: " + "\n")
        for i, task in enumerate(todo_list):
            file.write(str(i + 1) + ") " + task + "\n")
        file.close()