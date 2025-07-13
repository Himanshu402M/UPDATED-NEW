#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20246767"))
API_HASH = environ.get("API_HASH", "40c77323994b4c8b3dfc38273955ed3b")
BOT_TOKEN = environ.get("BOT_TOKEN", "7715030771:AAE3XzN_ZZ0RJJ6vf2hXE1QAx9jZKPcQsTw")
OWNER = int(environ.get("OWNER", "2001332759"))
CREDIT = environ.get("CREDIT", "〱⏤͟͞𝙃 𝙈🐦‍🔥 〄 ♥️ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝ᡃ⃝🦋")
AUTH_USER = os.environ.get('AUTH_USERS', '8034639315').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
