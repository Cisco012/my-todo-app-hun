import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("Tennivalók appom!!")
st.subheader("Tennivalókat tudsz hozzáadni / törölni ha már elkészültek")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:

        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input("Adj hozzá tennivalót: ",
              placeholder="Ide írhatod....",
              on_change=add_todo, key='new_todo')


