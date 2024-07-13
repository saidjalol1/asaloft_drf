from django.conf import settings
from io import BytesIO
from urllib.parse import urljoin
import requests
from .models import Product, ProductImages

TELEGRAM_BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID
BASE_URL = settings.BASE_URL


def send_order_notification(order):
    overall_message = f"Buyurtma-{order.id}\n\nYangi buyurtma qabul qilindi!\n\n"
    overall_message += f"Ism-Familiaysi: {order.full_name}\n"
    overall_message += f"Telefon raqami: {order.phone_number}\n"
    overall_message += f"Address: {order.address}\n\n"
    
    send_telegram_message(overall_message)

    for item in order.items.all():
        product = item.product
        product_message = f"Nomi: {product.name}\n"
        product_message += f"  o'lchamlari: {product.dimensions}\n"
        product_message += f"  Ramkasi: {product.frame}\n"
        product_message += f"  Materiali: {product.material}\n"
        product_message += f"  Bo'yoq turi: {product.paint_type}\n"
        product_message += f"  Narxi: {product.price}\n"
        product_message += f"  Soni: {item.quantity}\n"
        product_message += f"  Summasi: {item.amount}\n"
        send_telegram_message(product_message)


def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
    }
    
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"Failed to send message: {response.status_code} - {response.text}")
