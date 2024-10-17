from fastapi import HTTPException, Request
from src.jwt_service import JwtService

async def auth_middleware(request: Request):
    if "Authorization" not in request.headers:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    
    if not request.headers["Authorization"].startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization header. Must start with 'Bearer <token>'")

    # Split the header to get the token
    # because the string contains "Bearer " before the token
    token = request.headers["Authorization"].split(" ")[1]
    
    # Verify the token and get the payload
    try:
        payload = JwtService.verify(token)
        # Add the payload to the request state
        # so the endpoint can access it
        request.state.authenticated = payload
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")