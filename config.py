# Bot Configuration Settings

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token_here"

# Trading Exchange Settings
EXCHANGE = "binance"  # Options: binance, coinbase, kraken
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"

# Trading Parameters
TRADING_PAIRS = ["BTC/USDT", "ETH/USDT", "ADA/USDT"]
INITIAL_BALANCE = 1000  # in USDT
MAX_POSITION_SIZE = 0.1  # 10% of balance per trade

# Risk Management
STOP_LOSS_PERCENT = 2  # 2% stop loss
TAKE_PROFIT_PERCENT = 5  # 5% take profit
MAX_OPEN_TRADES = 3

# Trading Strategy
STRATEGY = "moving_average"  # Options: moving_average, rsi, bollinger_bands
MA_SHORT = 10
MA_LONG = 30

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "trading_bot.log"

# Database
DATABASE_URL = "sqlite:///trading_bot.db"