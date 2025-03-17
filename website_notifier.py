# website_notifier.py

import aiohttp
from config import WEBSITE_ENDPOINT

async def send_to_website(tx_data):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(WEBSITE_ENDPOINT, json=tx_data) as response:
                if response.status == 200:
                    print("Transaction data sent to website successfully.")
                else:
                    print("Failed to send data to website, status:", response.status)
        except Exception as e:
            print("Error sending data to website:", e)
