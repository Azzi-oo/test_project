from pydantic import BaseModel, validator, ValidationError


class Post(BaseModel):
    id: int
    title: str


    @validator("id")
    def check_id(cls, v):
        if v > 2:
            raise ValidationError('Id is not less than two')
        else:
            return v
