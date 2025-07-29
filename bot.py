from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Your bot logic here
print(f"Bot token loaded: {BOT_TOKEN[:10]}...")  # Partially mask for testing
