import os

from aiogram import types
from aiogram.utils import executor

from create_bot import bot, dp
from kb import start_kb, show_report_kb, send_report_kb
from requests_to_backend import add_item, show_report, send_report

from src import utils


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(utils.WELCOME_TEXT, reply_markup=start_kb)


@dp.message_handler(commands=['Вывести_отчет'])
async def show_reports(message: types.Message):
    await message.answer('Выберите месяц: ', reply_markup=show_report_kb)


@dp.callback_query_handler(lambda callback: callback.data.startswith('show_report'))
async def show_report_callback(callback: types.CallbackQuery):
    await callback.message.answer(show_report(callback.data[-1]))
    await bot.send_photo(callback.from_user.id, photo=open('report_common.pdf', 'rb'))
    os.remove('report_common.pdf')


@dp.message_handler(commands=['Отправить_отчет_на_почту'])
async def start(message: types.Message):
    await message.answer('Выберите месяц: ', reply_markup=send_report_kb)


@dp.callback_query_handler(lambda callback: callback.data.startswith('send_report'))
async def show_report_callback(callback: types.CallbackQuery):
    await callback.message.answer(send_report(callback.data[-1]))
    os.remove('report_common.pdf')


@dp.message_handler()
async def add_item_command(message: types.Message):
    splitted_message = message.text.split(' - ')
    is_correct_format = utils.is_correct_format(splitted_message)
    if is_correct_format:
        add_item(splitted_message)
        await message.answer('Статья добавлена')
    else:
        await message.answer('Неверный формат сообщения')


executor.start_polling(dp, skip_updates=True)
