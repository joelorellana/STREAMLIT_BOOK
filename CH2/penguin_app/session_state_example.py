import streamlit as st

st.title("My To-Do List Creator")
if 'my_todo_list' not in st.session_state:
    st.session_state.my_todo_list = ['Buy groceries', 'Learn Streamlit', 'Watch a movie']

# st.write('My current To-Do list is: ', my_todo_list)
new_todo = st.text_input("Enter new To-Do")
if st.button('Add new To-Do'):
    st.write('Adding a new item to the list...')
    st.session_state.my_todo_list.append(new_todo)
st.write('My new To-Do list is: ', st.session_state.my_todo_list)