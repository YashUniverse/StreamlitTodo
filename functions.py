FilePath = "todos.txt"


def get_todos(filepath=FilePath):
    """Read a text file and return a list of
     todo items"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(todoarg, filepath=FilePath):
    '''
    write the todos into the txt

    '''
    with open(filepath, 'w') as file:
        todos_local = file.writelines(todoarg)


if __name__ == "__main__":
    listitem = get_todos()
    todo = input("Enter a new todo")
    if not todo.endswith('\n'):
        todo = todo + '\n'

    listitem.append(todo)
    write_todos(listitem)




