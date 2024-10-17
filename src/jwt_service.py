from typing import Union
import jwt # import the jwt library
import os # import the os library
import datetime # import the datetime library

class JwtService:
        
    def sign(sub: Union[str, int]) -> str:
        secret = os.getenv("JWT_SECRET") # The secret key used to sign the token
        ttl = datetime.timedelta(seconds=int(os.getenv("JWT_TTL"))) # The time-to-live of the token
        
        iat = datetime.datetime.now(datetime.timezone.utc) # When the token was issued
        exp = iat + ttl # Set the expiration time of the token
        payload = {"sub": sub, "iat": iat, "exp": exp} # The payload of the token
        token = jwt.encode(payload, algorithm="HS256", key=secret) # Create the token
        
        return token
    
    def verify(token: str) -> dict:
        secret = os.getenv("JWT_SECRET") # The secret key used to sign the token
        payload = jwt.decode(token, algorithms=["HS256"], key=secret)
        
        return payload