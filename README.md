# Python JWT Demo
A simple Python FastAPI application that demonstrates JWT authentication.

# Get Started

## Setup virtual environment
1. Create the virtual environment
```
python -m venv venv
```

2. Activate the virtual environment
```bash
source venv/bin/activate 2>/dev/null || venv\Scripts\activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null && echo "Virtual environment activated." || echo "Failed to activate virtual environment."
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Setup .env

1. Create the .env file
```
cp .env.example .env
```

2. Generate and copy past a new secret
```
python ./new_secret.py
```

## Run the application
Start the server and go to `http://localhost:8000` in your browser.
```bash
fastapi dev main.py
```

# Documentation
The project contains three important files:
- main.py
- src/auth_middleware.py
- src/jwt_service.py

## main.py
Creates the FastAPI application with three endpoints:
- **GET** `/`: Returns a HTML page with a form to login.
- **POST** `/login`: Authenticates the user and returns a JWT token.
- **GET** `/me`: Requires a JWT token to access and returns the authenticated user's information.

## src/auth_middleware.py
Defines a method `auth_middleware` that checks if the request contains a valid JWT token in the `Authorization` header. If the token is valid, the decoded contents are stored in the request's state.

## src/jwt_service.py
Defines a class with two static methods:
- `sign`: Generates a JWT token with the provided payload.
- `verify`: Verifies the JWT token and returns the decoded contents.