import streamlit as sl
import functions

todos = functions.get_todos()


def add_todo():
    todo = sl.session_state["new_todo"].strip()
    todo = todo + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    sl.session_state["new_todo"] = ""


sl.title("My Todo App")
sl.subheader("This is a subheader")
sl.write("A simple app to increase your productivity")


for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()


sl.text_input(
    label="Todo",
    label_visibility="hidden",
    placeholder="Enter a todo...",
    on_change=add_todo,
    key="new_todo",
)
