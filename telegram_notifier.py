import aiohttp
import ssl
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID

def escape_markdown(text):
    # Reserved characters in MarkdownV2 that must be escaped
    escape_chars = r'_*\[\]()~`>#+\-=|{}.!'
    for char in escape_chars:
        text = text.replace(char, f"\\{char}")
    return text

async def send_telegram_notification(tx_data):
    # Ensure the transaction hash begins with '0x'
    tx_hash = tx_data.get('tx_hash')
    if not tx_hash.startswith("0x"):
        tx_hash = "0x" + tx_hash

    # Ensure the addresses begin with '0x'
    from_addr = tx_data.get('from_addr')
    if not from_addr.startswith("0x"):
        from_addr = "0x" + from_addr
    to_addr = tx_data.get('to_addr')
    if not to_addr.startswith("0x"):
        to_addr = "0x" + to_addr

    # Define clickable URLs (adjust these URLs as needed for your explorer)
    tx_url = f"https://testnet.monadexplorer.com/tx/{tx_hash}"
    from_url = f"https://testnet.monadexplorer.com/address/{from_addr}"
    to_url = f"https://testnet.monadexplorer.com/address/{to_addr}"
    block_url = f"https://testnet.monadexplorer.com/block/{tx_data.get('blockNumber')}"

    # Escape dynamic values for MarkdownV2 inline code formatting
    amount_str = escape_markdown(str(tx_data.get('amount')) + " MON")
    block_str = escape_markdown(str(tx_data.get('blockNumber')))
    from_trunc = escape_markdown(from_addr[:6] + "..." + from_addr[-4:])
    to_trunc = escape_markdown(to_addr[:6] + "..." + to_addr[-4:])

    # Build the message using MarkdownV2 formatting.
    # The block field in the message remains clickable.
    message = (
        "🚨 Large MON Transfer Alert\\!\n\n"
        "💰 Amount: [`" + amount_str + "`](" + block_url + ")\n"
        "📦 Block: [`" + block_str + "`](" + block_url + ")\n"
        "📤 From: [`" + from_trunc + "`](" + from_url + ")\n"
        "📥 To: [`" + to_trunc + "`](" + to_url + ")\n"
        "🔍 [View Transaction](" + tx_url + ")"
    )

    # Build an inline keyboard with four buttons: Block, From, To, Tx
    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "Block", "url": block_url},
                {"text": "From", "url": from_url},
                {"text": "To", "url": to_url},
                {"text": "TxHash", "url": tx_url}
            ]
        ]
    }

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHANNEL_ID,  # Ensure this is in the proper format, e.g., "-100XXXXXXXXXX" for channels
        "text": message,
        "parse_mode": "MarkdownV2",
        "reply_markup": reply_markup
    }

    # Create an SSL context that does not verify certificates (development only)
    ssl_context = ssl._create_unverified_context()
    connector = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=connector) as session:
        try:
            # Use json=payload so that the payload is properly JSON-encoded
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    print("Telegram notification sent.")
                else:
                    error_text = await response.text()
                    print("Failed to send Telegram notification.", response.status, error_text)
        except Exception as e:
            print("Exception during Telegram notification:", e)
