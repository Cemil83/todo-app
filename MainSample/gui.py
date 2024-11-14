import functions
import FreeSimpleGUI as sg
import time

sg.theme('Black')

label_time=sg.Text("",key="clock")
label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter a todo",key="todo")
add_button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(),key='todos',
                    enable_events=True,size=[35,10])
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button=sg.Button("Exit")

window=sg.Window('My To-Do App',
                 layout=[[label_time],
                         [label],
                         [input_box,add_button],
                         [list_box,edit_button,complete_button],
                         [exit_button]],
                 font=('Helvetica',20))

while True:
    event,values=window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))

    match event:
        case 'Add':
            todos=functions.get_todos()
            new_todo=values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                todo_to_edit=values['todos'][0]
                new_todo=values['todo']

                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.",font=("Helvetica",20))

        case 'Complete':
            try:
                todos=functions.get_todos()
                todo_to_remove=values['todos'][0]
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                sg.popup("Please select an item first.",font=("Helvetica",20))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()