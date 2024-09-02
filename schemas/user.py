from pydantic import BaseModel, validator
from enums.user_enums import Genders


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders

    @validator('email')
    def check_that_email_addrestt(cls, email):
        if '0' in email:
            return email
        else:
            raise ValueError('Error')
