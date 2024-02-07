# Import necessary libraries
import streamlit as st

# Define a Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        new_node.next = self.head
        self.head = new_node

    def remove_task(self, task):
        current = self.head
        previous = None

        while current is not None:
            if current.data == task:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                break
            previous = current
            current = current.next

    def display_tasks(self):
        tasks = []
        current = self.head

        while current is not None:
            tasks.append(current.data)
            current = current.next

        tasks.reverse()

        return tasks

# Create a Streamlit app
def main():
    st.title("To-Do List App with Linked List")

    # Initialize a single linked list
    if 'tasks_list' not in st.session_state:
        st.session_state.tasks_list = LinkedList()

    # Sidebar for adding tasks
    task_input = st.sidebar.text_input("Add Task:")
    if st.sidebar.button("Add"):
        if task_input:
            st.session_state.tasks_list.add_task(task_input)

    # Sidebar for removing tasks
    task_to_remove = st.sidebar.text_input("Remove Task:")
    if st.sidebar.button("Remove"):
        if task_to_remove:
            st.session_state.tasks_list.remove_task(task_to_remove)

    # Main content to display tasks
    st.write("## Your To-Do List:")
    tasks = st.session_state.tasks_list.display_tasks()

    if not tasks:
        st.write("No tasks yet. Add some tasks using the sidebar!")

    for i, task in enumerate(tasks, start=1):
        st.write(f"{i}. {task}")

if __name__ == "__main__":
    main()