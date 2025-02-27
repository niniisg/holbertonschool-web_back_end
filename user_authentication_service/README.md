#  User authentication service

This project demonstrates how to implement a basic authentication system using Flask for learning purposes. While in production environments, it is advised to use established frameworks and modules like `Flask-User`, this project walks you through building the authentication mechanism step by step to deepen your understanding.

### Learning Objectives

At the end of this project, you should be able to:

- Declare API routes in a Flask app.
- Handle cookies for session management.
- Retrieve form data from HTTP requests.
- Return appropriate HTTP status codes.

## Requirements

### Python Version:
- Python 3.9 (Ubuntu 20.04 LTS)

### Libraries:
- Flask
- SQLAlchemy
- Requests module (for interacting with APIs)
- Pycodestyle for code style checks

### Code Style:
- Your code should adhere to the **pycodestyle** (version 2.5).

### Documentation:
- All files should include proper documentation for modules, classes, and functions.
- The first line of all Python files must be: `#!/usr/bin/env python3`
- Each function, class, and module should include a clear description of its purpose.

## Project Structure

- **auth.py**: Contains the logic for authentication.
- **db.py**: Contains the database-related functionalities using SQLAlchemy.
- **app.py**: The main Flask app where the routes are declared.
- **requirements.txt**: A list of dependencies.
- **README.md**: This file with project details and instructions.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
