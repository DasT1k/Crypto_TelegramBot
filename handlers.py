from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import requests

from keyboards import price_menu, main_menu

router = Router()


@router.message(F.text, Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Bot provide actual crypto price and something else", reply_markup=main_menu)


@router.message(F.text, Command("price"))
@router.message(F.text == "Prices")
async def price_handler(msg: Message):
    # TODO: после нажатия этой кнопки основное меню должно пропадать, но ReplyKeyboardRemove() не срабатывает
    await msg.answer("Send coin symbol or select from menu to get actual price", reply_markup=price_menu)


@router.message(F.text)
async def message_handler(msg: Message):
    response = requests.get(url=f'https://api.binance.com/api/v3/ticker/price?symbol={msg.text.upper()}USDT')
    data = response.json()
    if "price" in data:  # если все ок и запрос вернул цену
        await msg.answer(f"{msg.text.upper()} price:  {data['price'].rstrip('0')}  usdt")
    elif "code" in data:  # если запрос вернул код ошибки (99% что введен неверный код символа)
        await msg.answer(data['msg'])
    else:  # например ситуация когда сервер недоступен и мы не получили никакого ответа
        await msg.answer("Something went wrong")


@router.callback_query(F.data == "BTC")
@router.callback_query(F.data == "ETH")
async def price_menu_handler(callback: CallbackQuery):
    response = requests.get(url=f'https://api.binance.com/api/v3/ticker/price?symbol={callback.data}USDT')
    data = response.json()
    if "price" in data:  # если все ок и запрос вернул цену
        await callback.message.answer(f"{callback.data} price:  {data['price'].rstrip('0')}  usdt")
        await callback.answer()  # подтверждение о доставке callback, иначе кнопка горит 30 сек
    elif "code" in data:  # если запрос вернул код ошибки (99% что введен неверный код символа)
        await callback.message.answer(data['msg'])
        await callback.answer()
    else:  # например ситуация когда сервер недоступен и мы не получили никакого ответа
        await callback.message.answer("Something went wrong")
        await callback.answer()
