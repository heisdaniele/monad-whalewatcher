# config.py

# Replace with your Monad node URL (ensure it supports websockets if needed)
NODE_URL = "wss://testnet-rpc.monad.xyz"

# Transfer threshold: Adjust based on your token's decimal precision.
# Now set to 50 MON (50 * 10^18 units)
TRANSFER_THRESHOLD = 50 * (10 ** 18)

# Telegram settings
TELEGRAM_BOT_TOKEN = "8162787715:AAEY0ADb0ZU_jHaqiZiT7bwEfRi2o01ltXI"
TELEGRAM_CHANNEL_ID = "-1002485583230"  # Use channel username or numeric ID

# Website endpoint (Flask server) to which transactions will be POSTed
WEBSITE_ENDPOINT = "http://localhost:5000/api/transactions"
