from pydantic import BaseModel, EmailStr

class CheckoutPayload(BaseModel):
    user_id: str
    email: EmailStr
    cpf: str
    amount: float
