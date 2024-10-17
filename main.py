from dotenv import load_dotenv # Import dotenv to load the .env file
from fastapi import FastAPI, Depends, Request # Import FastAPI for creating the app and Depends to use dependencies (fx. middleware)
from fastapi.responses import HTMLResponse # Import HTMLResponse to return HTML content

from src.jwt_service import JwtService # A service to sign and verify JWT tokens
from src.auth_middleware import auth_middleware # A custom middleware to authenticate the user

load_dotenv() # Load the .env file

# Create a new FastAPI app
app = FastAPI()

# A list of dummy users
dummy_users = [
    { "id": 1, "username": "test", "password": "test" },
    { "id": 2, "username": "John", "password": "John" }
]

# This endpoint is protected by the auth_middleware
# which means the user must provide a valid JWT token
# in the Authorization header to get access
# to its content.
@app.get("/me")
def me_api(request: Request, user=Depends(auth_middleware)):
    authenticated = request.state.authenticated
    # find the user authenticated user by the sub claim
    # which is equal to the user's id
    user = next((u for u in dummy_users if u["id"] == authenticated["sub"]), None)
    # return the user's username and id
    return {"username": user["username"], "id": user["id"]}

@app.post("/login")
def login_api(request: dict):
    username = request.get("username")
    password = request.get("password")
    if not username: return {"error": "Username is required"}
    if not password: return {"error": "Password is required"}
    
    # Normally you would look the user in the database
    # and compare hashed passwords but I choose not to
    # include that in this example to keep it simple.
    # The focus is on the JWT part.
    user = next((u for u in dummy_users if u["username"] == username and u["password"] == password), None)
    if not user:
        return {"error": "Invalid username or password"}
    
    # Create a new token with the user's id
    # as the payload's subject claim
    token = JwtService.sign(sub=user["id"])
    # Return the token to the user
    # so they can use it for authentication
    # in future requests
    return {"token": token}

# An endpoint that returns a html page
# where the user can login
@app.get("/", response_class=HTMLResponse)
def login_view():
    with open("templates/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
