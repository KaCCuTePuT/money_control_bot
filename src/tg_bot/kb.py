import datetime

from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь',
}

b1 = KeyboardButton('/Вывести_отчет')
b2 = KeyboardButton('/Отправить_отчет_на_почту')
b3 = KeyboardButton('/Вывести_записи_для_удаления')
start_kb = ReplyKeyboardMarkup()
start_kb.add(b1).add(b3).add(b2)

# Клавиатура для отправки отчета в tg
months_buttons_show_report = [InlineKeyboardButton(text=months[i], callback_data=f'show_report_{i}') for i in range(1, datetime.date.today().month + 1)]
show_report_kb = InlineKeyboardMarkup(row_width=1)
show_report_kb.add(*months_buttons_show_report)

# Клавиатура для отправки отчета на почту
months_buttons_send_report = [InlineKeyboardButton(text=months[i], callback_data=f'send_report_{i}') for i in range(1, datetime.date.today().month + 1)]
send_report_kb = InlineKeyboardMarkup(row_width=1)
send_report_kb.add(*months_buttons_send_report)
