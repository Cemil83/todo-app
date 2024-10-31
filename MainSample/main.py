# from functions import get_todos,write_todos
import functions
import time

now=time.strftime("%b %d,%Y %H:%M:%S")
print("it is :",now)


while True:
    user_action = input("Show,Add,Edit,Complete or Exit :")
    user_action = user_action.strip()

    if user_action.startswith('add') :
        todo = user_action[4:]+'\n'
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        todos=functions.get_todos()

        todos.append(todo)
        #  file = open('todos.txt', 'w')
        #  file.writelines(todos)
        #  file.close()
        functions.write_todos(todos,'todos.txt')

    elif user_action.startswith('show'):
        todos=functions.get_todos()

        for index, item in enumerate(todos):
            row = f"{index + 1}.{item}"
            print(row.strip("\n"))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            # test
            todos=functions.get_todos()

            new_todo = input("Enter new todo:")
            todos[number]=new_todo +'\n'

            functions.write_todos(todos,'todos.txt')

        except ValueError:
            print("Your command is not valid")
            continue

        except IndexError:
            print ("There is no item with that number.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[8:])
            todos=functions.get_todos()

            index=number-1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos,'todos.txt')

            message=f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print ("There is no item with that number.")
            continue

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Comment is not valid!!")

print("Goodbye")