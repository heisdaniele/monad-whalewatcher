# Monad Blockchain Watcher

A real-time monitoring system for the Monad blockchain that tracks large transfers and sends notifications via Telegram and a web interface.

## Features

- Real-time monitoring of Monad blockchain transactions
- Telegram notifications for large transfers
- Web interface with real-time updates using WebSocket
- Configurable transfer threshold

## Prerequisites

- Python 3.9+
- A Telegram bot token
- Access to Monad blockchain node

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/monad-watcher.git
cd monad-watcher
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file and configure your settings:
```bash
cp .env.example .env
```

5. Edit the `.env` file with your configuration values.

## Usage

1. Start the web server:
```bash
python server.py
```

2. In a separate terminal, start the blockchain listener:
```bash
python main.py
```

3. Open http://localhost:5000 in your browser to view the transaction dashboard.

## Configuration

Edit the `.env` file to configure:
- `NODE_URL`: Your Monad blockchain node URL
- `TRANSFER_THRESHOLD`: Minimum amount for transaction notifications
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `TELEGRAM_CHANNEL_ID`: Your Telegram channel ID
- `WEBSITE_ENDPOINT`: Your web server endpoint

## License

MIT

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
