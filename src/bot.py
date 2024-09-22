import asyncio
import logging
from typing import Final

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import Config
from .donation_alerts import TelegramAlertsHandler

_config = Config()

TOKEN: Final[str] = _config.bot_token
CHAT_ID: Final[int] = _config.reciever_chat_id
DONATION_ALERTS_TOKEN: Final[str] = _config.donation_alerts_token


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    donation_handler = TelegramAlertsHandler(
        bot,
        CHAT_ID,
        DONATION_ALERTS_TOKEN
    )

    dp.startup.register(donation_handler.connect)
    await dp.start_polling(bot)


def run():
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
