# config.py

import os
from dotenv import load_dotenv

load_dotenv()

NODE_URL = os.getenv('NODE_URL', 'wss://testnet-rpc.monad.xyz')
TRANSFER_THRESHOLD = int(os.getenv('TRANSFER_THRESHOLD', str(50 * (10 ** 18))))
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
WEBSITE_ENDPOINT = os.getenv('WEBSITE_ENDPOINT', 'http://localhost:5000/api/transactions')
