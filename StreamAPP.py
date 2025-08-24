import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todod = st.session_state['new_todo'] + "\n"
    todos.append(todod)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This app is to increase your productivity")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todoi{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f'todoi{index}']
        st.rerun()

st.text_input(label='', placeholder="add new todo", on_change=add_todo, key="new_todo")



