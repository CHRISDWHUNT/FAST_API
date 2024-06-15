from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import database, models, utils, oauth2, schemas

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    login_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials.")
    if not user:
        raise login_exception

    if not utils.varify(user_credentials.password, user.password):
        raise login_exception

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}