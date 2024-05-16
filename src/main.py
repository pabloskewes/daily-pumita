import os

from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")


def send_welcome(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hola!")


def echo_all(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(API_KEY)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start and /help command handler
    dispatcher.add_handler(CommandHandler(["start", "help"], send_welcome))

    # Register the message handler to echo all messages
    dispatcher.add_handler(
        MessageHandler(
            Filters.text & ~Filters.command,
            echo_all,
        )
    )

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, 
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == "__main__":
    main()
