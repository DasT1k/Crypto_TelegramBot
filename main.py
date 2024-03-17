import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router


async def main():
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # HTML разметка сообщений для избежания проблем с экранированием символов
    dp = Dispatcher(storage=MemoryStorage())  # все данные бота, которые мы не сохраняем в БД, будут стёрты при перезапуске
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)  # удаляем все обновления, которые произошли после последнего
    # завершения работы бота (нужно, чтобы бот обрабатывал только те сообщения, которые пришли ему непосредственно во время его работы, а не за всё время)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
