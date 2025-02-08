from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def query_db(query, params=()):
    conn = sqlite3.connect("emdatabase.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route("/")
def home():
    return "Chat Assistant is Running!"

@app.route("/query", methods=["POST"])
def handle_query():
    data = request.json
    user_query = data.get("query", "").lower()

    if "employees in" in user_query:
        dept = user_query.split("employees in ")[-1].strip()
        result = query_db("SELECT Name FROM Employees WHERE Department = ?", (dept,))
        return jsonify({"employees": [row[0] for row in result]})

    elif "manager of" in user_query:
        dept = user_query.split("manager of ")[-1].strip()
        result = query_db("SELECT Manager FROM Departments WHERE Name = ?", (dept,))
        return jsonify({"manager": result[0][0] if result else "Not found"})

    elif "hired after" in user_query:
        date = user_query.split("hired after ")[-1].strip()
        result = query_db("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
        return jsonify({"employees": [row[0] for row in result]})

    elif "salary expense for" in user_query:
        dept = user_query.split("salary expense for ")[-1].strip()
        result = query_db("SELECT SUM(Salary) FROM Employees WHERE Department = ?", (dept,))
        return jsonify({"total_salary": result[0][0] if result else 0})

    return jsonify({"error": "Unsupported query"})

if __name__ == "__main__":
    app.run(debug=True)
