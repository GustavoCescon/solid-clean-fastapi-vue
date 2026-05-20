# infrastructure/adapters/sendgrid_email.py
from app.modules.user.domain.ports.email_service import EmailService

class SendgridEmailAdapter(EmailService):

    def send_welcome(self, email: str, name: str):
      pass