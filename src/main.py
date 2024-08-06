import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.getenv("TELEGRAM_BOT_TOKEN")


# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am your Telegram bot.")


# Function to send a text message
async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = " ".join(context.args)
    if message:
        await update.message.reply_text(f"Sending: {message}")
    else:
        await update.message.reply_text("Please provide a message to send.")


# Function to send an image
async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Check if an image path is provided
    if context.args:
        image_path = context.args[0]
        try:
            with open(image_path, "rb") as image_file:
                await update.message.reply_photo(photo=image_file)
        except FileNotFoundError:
            await update.message.reply_text(
                f"Error: Image file not found at {image_path}"
            )
    else:
        await update.message.reply_text("Please provide the path to an image file.")


# Main function
def main() -> None:
    # Create the Application and pass it your bot's token
    application = ApplicationBuilder().token(API_KEY).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("send", send_message))
    application.add_handler(CommandHandler("image", send_image))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
