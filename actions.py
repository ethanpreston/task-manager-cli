from vim import get_user_input_with_vim
import sqlite3
from display import display


def connect_to_database():
    # Connect to task_manager database and return the connection and cursor
    connection = sqlite3.connect('task_manager.db')
    connection_cursor = connection.cursor()
    query = "CREATE TABLE IF NOT EXISTS tasks (task TEXT PRIMARY KEY, priority INT, due_date DATETIME, category TEXT," \
            " completed INT)"
    connection_cursor.execute(query)
    query_2 = "CREATE TABLE IF NOT EXISTS descriptions (task TEXT PRIMARY KEY, description TEXT)"
    connection_cursor.execute(query_2)
    return connection, connection_cursor


# Add a task to the task manager
def add(task, due_date=None, priority=None, category=None, completed=0):
    conn, cursor = connect_to_database()
    query = "INSERT OR REPLACE INTO tasks (task, priority, due_date, category, completed) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (task, priority, due_date, category, completed))
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection


# Delete a task from the task manager
def delete(task):
    conn, cursor = connect_to_database()
    # Delete the task from the table
    query = "DELETE FROM tasks WHERE task = ?"
    cursor.execute(query, (task,))
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection


# Add a description to a task
def describe(task):
    conn, cursor = connect_to_database()
    description = get_user_input_with_vim()
    cursor.execute("INSERT OR REPLACE INTO descriptions (task, description) VALUES (?, ?)", (task, description))
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection


def categorize(task, category):
    conn, cursor = connect_to_database()
    # Update the category of the task in the table
    query = "UPDATE tasks SET category = ? WHERE task = ?"
    cursor.execute(query, (category, task))
    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()


def list_category(category):
    conn, cursor = connect_to_database()
    # Retrieve the entries under the specified category
    query = "SELECT * FROM tasks WHERE category = ?"
    cursor.execute(query, (category,))
    # Fetch all the rows returned by the query
    rows = cursor.fetchall()
    # Print the entries
    display(rows)
    # Close the connection
    conn.close()


def list_all():
    conn, cursor = connect_to_database()
    query = "SELECT * FROM tasks"
    cursor.execute(query, )
    rows = cursor.fetchall()
    display(rows)
    conn.close()


# Mark a task as complete
def complete(task):
    conn, cursor = connect_to_database()
    query = "UPDATE tasks SET completed = ? WHERE task = ?"
    cursor.execute(query, (1, task))
    conn.commit()
    conn.close()


# Clear all completed tasks from the database
def clear_completed():
    conn, cursor = connect_to_database()
    query = "DELETE FROM tasks WHERE completed = ?"
    cursor.execute(query, (1,))
    conn.commit()
    conn.close()


def edit_due_date(task, due_date):
    conn, cursor = connect_to_database()
    # Update the due date of the task in the table
    query = "UPDATE tasks SET due_date = ? WHERE task = ?"
    cursor.execute(query, (due_date, task))
    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()


def edit_priority(task, priority):
    conn, cursor = connect_to_database()
    query = "UPDATE tasks SET priority = ? WHERE task = ?"
    cursor.execute(query, (priority, task))
    conn.commit()
    conn.close()


def get(task, attribute):
    conn, cursor = connect_to_database()
    if attribute == "description":
        query = "SELECT description FROM descriptions WHERE task = ?"
        cursor.execute(query, (task,))
        task_items = cursor.fetchall()
        print()
        print(f"Description for {task}: ")
    else:
        query = f"SELECT {attribute} FROM tasks WHERE task = ?"
        cursor.execute(query, (task,))
        task_items = cursor.fetchall()
        indices = {'priority': 1, 'due_date': 2, 'category': 3, 'completed': 4}
        print(f"{attribute} for {task}: {task_items[indices[attribute]]}")

