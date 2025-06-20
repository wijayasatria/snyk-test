import sqlite3

# Example of insecure user input handling
def get_user_data(username):
    # Vulnerable to SQL Injection
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    
    # Directly using user input in SQL query without sanitization
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    
    user_data = cursor.fetchone()
    
    # If user_data is None, it means user was not found
    if user_data:
        return user_data
    else:
        return "User not found"

# Storing passwords insecurely
def store_password(username, password):
    # Insecure password storage
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    
    # No hashing of passwords (vulnerable to password theft)
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()

# Insecure handling of sensitive data
def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Store user credentials insecurely
    store_password(username, password)
    
    # Retrieve user data without validating input
    user_data = get_user_data(username)
    print(user_data)

if __name__ == "__main__":
    main()
