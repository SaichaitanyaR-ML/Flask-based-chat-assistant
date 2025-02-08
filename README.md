# Flask-based-chat-assistant
# Chat Assistant for SQLite Database

## Overview
This project is a Flask-based chat assistant that interacts with an SQLite database.
It processes user queries in natural language, converts them into SQL, and returns relevant results.

## Features
- List all employees in a department
- Find department managers
- List employees hired after a certain date
- Calculate total salary expenses per department
- Handles errors gracefully (e.g., incorrect department names)
- ## Known Limitations
- Cannot handle very complex queries outside the defined logic.
- Assumes user input is well-formed.
- Uses a simple rule-based approach; future improvements could involve NLP models.
- ## Future Improvements
- Implement NLP-based query parsing.
- Expand database functionality.
- Deploy using Docker for easier scalability.

