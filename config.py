# config.py

import os
from dotenv import load_dotenv

load_dotenv()

NODE_URL = os.getenv('NODE_URL', 'wss://testnet-rpc.monad.xyz')
TRANSFER_THRESHOLD = int(os.getenv('TRANSFER_THRESHOLD', '50000000000000000000'))
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
WEBSITE_ENDPOINT = os.getenv('WEBSITE_ENDPOINT', 'http://localhost:5000/api/transactions')

# Validate configuration
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in .env file")
if not TELEGRAM_CHANNEL_ID:
    raise ValueError("TELEGRAM_CHANNEL_ID is not set in .env file")
