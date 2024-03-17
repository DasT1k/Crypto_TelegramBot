from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

prices = [
        [InlineKeyboardButton(text="Bitcoin", callback_data="BTC"),
         InlineKeyboardButton(text="Ethereum", callback_data="ETH")]
    ]
price_menu = InlineKeyboardMarkup(inline_keyboard=prices, input_field_placeholder="Enter coin symbol")

menu = [
    [KeyboardButton(text="Prices"), KeyboardButton(text="Something else")]
]
main_menu = ReplyKeyboardMarkup(keyboard=menu, resize_keyboard=True, input_field_placeholder="Select an option")
