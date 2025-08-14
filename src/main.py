from aiohttp import web

from src.settings import config_server, config_telegram_client
from src.telegram import TelegramClient

telegram_client = TelegramClient(
    api_id = config_telegram_client['api_id'],
    api_hash = config_telegram_client['api_hash'],
)