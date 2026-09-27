from fastapi import FastAPI
from src.models import CheckoutPayload
from src.services.payment_service import process_checkout_logic

app = FastAPI(title="Pace Enterprise API")

@app.post("/api/v1/checkout")
async def checkout_endpoint(payload: CheckoutPayload):
    # O endpoint fica limpo, delegando para o service
    result = await process_checkout_logic(payload)
    return result
