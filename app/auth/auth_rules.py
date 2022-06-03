from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import HTTPException, status, Depends

from app.auth.auth_users import authorized_users, pwd_context

security = HTTPBasic()

def get_auth_status(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    if not(authorized_users.get(username)) or not(pwd_context.verify(credentials.password, authorized_users[username]['hashed_password'])):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True

def get_admin_auth_status(credentials: HTTPBasicCredentials = Depends(security)):
    username = "admin"
    if not(authorized_users.get(username)) or not(pwd_context.verify(credentials.password, authorized_users[username]['hashed_password'])):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True