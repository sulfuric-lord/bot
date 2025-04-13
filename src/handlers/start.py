from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from src.keyboards.inline import get_start_keyboard
from src.cfg import *

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=PICTURES["start"],
                         caption=("Мяу-мяу! 🐾\n"
                         "Добро пожаловать в наше кафе с вкусняшками! Заходи, выбирай вкус, и мы с радостью приготовим для тебя что-то особенное! 💕\n"
                         "Взаимодействуй с кнопками, выбери в меню понравившийся моти и твой заказ будет готов! 🐈"),
                         reply_markup=get_start_keyboard())

@router.message(F.photo)
async def get_id(message: Message):
    photo_data = message.photo[-1]
    await message.reply(f"{photo_data}")