import asyncio
import ssl
from web3 import Web3
from config import NODE_URL, TRANSFER_THRESHOLD
from telegram_notifier import send_telegram_notification
from website_notifier import send_to_website

# Create an SSL context for testing (not for production)
ssl_context = ssl._create_unverified_context()

w3 = Web3(Web3.WebsocketProvider(NODE_URL, websocket_kwargs={"ssl": ssl_context}))

# Set to track processed transactions to avoid duplicates
processed_tx_hashes = set()

# Define the token's decimal factor (1 MON = 10^18 units)
MON_DECIMALS = 10 ** 18

async def listen_to_blocks():
    print("Starting blockchain listener...")
    current_block = w3.eth.block_number
    while True:
        try:
            latest_block = w3.eth.block_number
            if latest_block > current_block:
                for block_number in range(current_block + 1, latest_block + 1):
                    print(f"Processing block: {block_number}")
                    block = w3.eth.get_block(block_number, full_transactions=True)
                    await process_block(block)
                current_block = latest_block
            await asyncio.sleep(5)  # Polling interval
        except Exception as e:
            print("Error in blockchain listener:", e)
            await asyncio.sleep(5)

async def process_block(block):
    for tx in block.transactions:
        # Check if the transaction value exceeds the threshold
        if tx.value and tx.value >= TRANSFER_THRESHOLD:
            tx_hash = tx.hash.hex()
            # Skip duplicate transactions
            if tx_hash in processed_tx_hashes:
                continue
            processed_tx_hashes.add(tx_hash)
            # Convert raw token amount to MON by dividing by 10^18
            human_amount = tx.value / MON_DECIMALS

            tx_data = {
                "tx_hash": tx_hash,
                "from_addr": tx["from"],
                "to_addr": tx.to,
                "amount": f"{human_amount:.2f}",  # Format to two decimal places
                "blockNumber": block.number,
            }
            print("Large transfer detected:", tx_data)
            await asyncio.gather(
                send_to_website(tx_data),
                send_telegram_notification(tx_data)
            )

if __name__ == "__main__":
    asyncio.run(listen_to_blocks())
