import sqlite3
from sqlite3 import Error

# Function to create a connection with a SQLite database
def create_connection():
    # Initialize the connection variable
    conn = None;
    try:
        # Connect to an in-memory SQLite database
        conn = sqlite3.connect(':memory:')  # creates a database in RAM
        return conn
    except Error as e:
        # Print the error message
        print(e)

    # Return the connection object
    return conn

# Function to close an existing connection with a SQLite database
def close_connection(conn):
    # Close the connection
    conn.close()

# Function to create a new table in a SQLite database
def create_table(conn, create_table_sql):
    try:
        # Create a cursor object
        c = conn.cursor()
        # Execute the SQL query to create a new table
        c.execute(create_table_sql)
    except Error as e:
        # Print the error message
        print(e)

# Function to insert new data into a table in a SQLite database
def insert_data(conn, table, data):
    with conn:
        # Create a cursor object
        c = conn.cursor()
        # Execute the SQL query to insert new data into the table
        c.execute(f"INSERT INTO {table} VALUES({data})")

# Function to select all data from a table in a SQLite database
def select_all_data(conn, table):
    with conn:
        # Create a cursor object
        c = conn.cursor()
        # Execute the SQL query to select all data from the table
        c.execute(f"SELECT * FROM {table}")
        # Fetch all the rows from the table
        rows = c.fetchall()

        # Print each row
        for row in rows:
            print(row)

# Function to update existing data in a table in a SQLite database
def update_data(conn, table, set_data, condition):
    with conn:
        # Create a cursor object
        c = conn.cursor()
