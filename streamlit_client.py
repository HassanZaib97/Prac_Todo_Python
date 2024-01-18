# streamlit_client.py
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
    new_todo_title = st.text_input("Enter Todo Title:")
    new_todo_description = st.text_input("Enter Todo Description:")
    if st.button("Create Todo"):
        if new_todo_title and new_todo_description:
            create_todo(new_todo_title, new_todo_description)

    # Test Update Todo
    st.header("Update Todo")
    update_todo_id = st.text_input("Enter Todo ID to Update:")
    updated_title = st.text_input("Enter Updated Todo Title:")
    updated_description = st.text_input("Enter Updated Todo Description:")
    if st.button("Update Todo"):
        if update_todo_id and updated_title and updated_description:
            update_todo(int(update_todo_id), updated_title, updated_description)

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

def create_todo(title, description):
    payload = {"title": title, "description": description}
    response = requests.post(f"{BASE_URL}/todos/", json=payload)
    display_response(response)

def update_todo(todo_id, title, description):
    payload = {"title": title, "description": description}
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
