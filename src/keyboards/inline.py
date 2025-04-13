from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_start_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📜 Меню", callback_data="menu"),
            InlineKeyboardButton(text="🎁 Акции", callback_data="promo")
        ],
        [
            InlineKeyboardButton(text="ℹ️ О нас", callback_data="about"),
            InlineKeyboardButton(text="📞 Поддержка", callback_data="support")
        ]
    ])