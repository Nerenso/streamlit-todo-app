FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Reads a text file and returns the list of todo items."""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """Accepts a todo list and writes it to the stored text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
