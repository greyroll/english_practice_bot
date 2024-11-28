import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.enums import ParseMode

from loguru import logger

from secret import secret_api_token
from handlers.user_handlers import UserHandlers

API_TOKEN = secret_api_token

# Включаем логирование
logger.add("logfile.log", level="DEBUG")

dp = Dispatcher()
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


dp.message.register(UserHandlers.start_command, Command(commands=["start"]))



async def main() -> None:
	await dp.start_polling(bot)


asyncio.run(main())
