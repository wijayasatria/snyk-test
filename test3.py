# Example Python application with multiple high-severity vulnerabilities

import json
import requests
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Vulnerable package: Flask < 1.0 (CVE-2018-1000656)
# It is vulnerable to Cross-Site Scripting (XSS) if templates are not properly escaped.

# Example SQLite database connection (no error handling for simplicity)
def get_db_connection():
    conn = sqlite3.connect('example.db')
    return conn

# Insecure deserialization (using eval)
def deserialize_data(data):
    try:
        return eval(data)  # This is insecure and can execute arbitrary code
    except Exception as e:
        print(f"Deserialization error: {e}")
        return None

# SQL Injection vulnerability
@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('id')
    query = f"SELECT * FROM users WHERE id = {user_id};"  # Vulnerable to SQL Injection
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return jsonify({'id': user[0], 'name': user[1]})
    else:
        return jsonify({'error': 'User not found'}), 404

# Using an outdated requests version with known vulnerabilities
def fetch_data(url):
    # Vulnerable package: requests < 2.25.1
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

@app.route('/data', methods=['GET'])
def data_endpoint():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    try:
        data = fetch_data(url)
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

# Main execution
if __name__ == "__main__":
    app.run(debug=True)
