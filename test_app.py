# test_app.py
import streamlit as st
import requests

# Set the base URL for your FastAPI server
BASE_URL = "http://localhost:8000"  # Update with your FastAPI server URL

def main():
    st.title("Todo CRUD Operations")

    # Test Get Todo by ID
    st.header("Get Todo by ID")
    todo_id = st.text_input("Enter Todo ID:")
    if st.button("Get Todo"):
        if todo_id:
            get_todo_by_id(int(todo_id))

    # Test Get All Todos
    st.header("Get All Todos")
    get_all_todos()

    # Test Create Todo
    st.header("Create Todo")
    new_todo_text = st.text_input("Enter Todo Text:")
    if st.button("Create Todo"):
        if new_todo_text:
            create_todo(new_todo_text)

    # Test Update Todo
    st.header("Update Todo")
    update_todo_id = st.text_input("Enter Todo ID to Update:")
    updated_text = st.text_input("Enter Updated Todo Text:")
    if st.button("Update Todo"):
        if update_todo_id and updated_text:
            update_todo(int(update_todo_id), updated_text)

    # Test Delete Todo
    st.header("Delete Todo")
    delete_todo_id = st.text_input("Enter Todo ID to Delete:")
    if st.button("Delete Todo"):
        if delete_todo_id:
            delete_todo(int(delete_todo_id))

def get_todo_by_id(todo_id):
    response = requests.get(f"{BASE_URL}/todos/{todo_id}")
    display_response(response)

def get_all_todos():
    response = requests.get(f"{BASE_URL}/todos/")
    display_response(response)

def create_todo(todo_text):
    payload = {"text": todo_text}
    response = requests.post(f"{BASE_URL}/todos/", json=payload)
    display_response(response)

def update_todo(todo_id, updated_text):
    payload = {"text": updated_text}
    response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=payload)
    display_response(response)

def delete_todo(todo_id):
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    display_response(response)

def display_response(response):
    st.subheader("API Response:")
    if response.status_code == 200:
        st.success("Operation Successful!")
        st.json(response.json())
    else:
        st.error(f"Error: {response.status_code}")
        st.text(response.text)

if __name__ == "__main__":
    main()
