import requests
import os

BOT_TOKEN = os.getenv("8854509623:AAFuAkw5EsMnAx0vUhPo1c3tb6pf5z5OLDU")
CHAT_ID = os.getenv("1757791401")

requests.post(
    f"https://api.telegram.org/bot8854509623:AAFuAkw5EsMnAx0vUhPo1c3tb6pf5z5OLDU/sendMessage",
    data={
        "chat_id": 1757791401,
        "text": "🚀 Your GitHub bot is working!"
    }
)
