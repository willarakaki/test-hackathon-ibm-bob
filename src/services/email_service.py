class ReceiptMailer:
    def __init__(self):
        self.server = "smtp.banco.com"
        
    def send_receipt(self, email: str, amount: float):
        # Lógica falsa de envio de e-mail
        return True
