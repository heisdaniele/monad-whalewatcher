# main.py

import asyncio
from blockchain_listener import listen_to_blocks

if __name__ == "__main__":
    try:
        asyncio.run(listen_to_blocks())
    except KeyboardInterrupt:
        print("Shutting down blockchain listener.")
