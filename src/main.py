import asyncio
from aiogram import Bot, Dispatcher
from cfg import *
from handlers import start

dp = Dispatcher()
dp.include_router(start.router)

async def main():
    print("Бот запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
