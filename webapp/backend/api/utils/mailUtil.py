from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List
from utils import config
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

settings = config.get_settings()


conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,  # Updated field
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS
)

async def send_email(subject: str, recipient: List, message: str):
    message = MessageSchema(
        subject=subject,
        recipients=recipient,
        body=message,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)


def load_html_template(template_path: str, context: dict) -> str:
    # Define the path to the directory containing the templates
    template_dir = os.path.dirname(template_path)
    
    # Initialize the Jinja2 Environment
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml'])  # Auto-escape HTML/XML content
    )
    
    # Load the template file
    template = env.get_template(os.path.basename(template_path))
    
    # Render the template with the provided context
    rendered_html = template.render(context)
    
    return rendered_html
