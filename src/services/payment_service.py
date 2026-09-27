import time
import requests
from src.models import CheckoutPayload
from src.services.email_service import ReceiptMailer

async def process_checkout_logic(payload: CheckoutPayload):
    # 1. Vazamento de PII (Privacidade)
    print(f"[LOG INFO] Iniciando transação. Cliente: {payload.email} | CPF: {payload.cpf}")
    
    # 2. Falha de Arquitetura (Bloqueio de Event Loop)
    # Chamada síncrona dentro de uma função async
    response = requests.post("https://api.gatewaypagamentos.com/v1/charge", json={"valor": payload.amount})
    time.sleep(1.5) # Simulando latência de rede
    
    if response.status_code == 200:
        # 3. Falha de Testabilidade (Acoplamento Forte)
        # Instanciando a classe diretamente na regra de negócio (sem injeção de dependência)
        mailer = ReceiptMailer()
        mailer.send_receipt(payload.email, payload.amount)
        
        return {"status": "Aprovado"}
    
    return {"status": "Recusado"}
