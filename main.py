
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    ChatJoinRequestHandler,
)

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

WELCOME_TEXT = """👑 NEXO TRADER ELITE में आपका स्वागत है!

आपकी Join Request स्वीकार कर ली गई है।

यहाँ आपकी VIP जानकारी और अपडेट मिलेंगे।
"""

async def approve_request(update: Update, context):
    request = update.chat_join_request
    user_id = request.from_user.id

    try:
        await request.approve()
        logging.info("Join request approved: %s", user_id)

        await context.bot.send_message(
            chat_id=user_id,
            text=WELCOME_TEXT
        )

    except Exception as error:
        logging.error("Error: %s", error)

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(approve_request))
    app.run_polling(
        allowed_updates=["chat_join_request"]
    )

if __name__ == "__main__":
    main()
  
