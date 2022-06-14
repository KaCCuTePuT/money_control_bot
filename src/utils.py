WELCOME_TEXT = 'Добро пожаловать в бот контроля бюджета.' \
               '\nДля быстрого добавления статьи расходов или доходов напишите сообщение в формате:' \
               '\n"Категория" - "Да/Нет(Расход или нет)" - ' \
               '\n"Описание(если несколько слов, то они должны быть отделены _ )" - ' \
               '\n"Сумма(только натуральное число)".' \
               '\nВозможные категории:' \
               '\n1) Donation;' \
                '\n2) Salary;' \
                '\n3) MTS_Piggybank;' \
                '\n4) Other;' \
                '\n5) Medicines;' \
                '\n6) Rent;' \
                '\n7) Food;' \
                '\n8) Phone;' \
                '\n9) Clothes;' \
                '\n10) Subscriptions;' \
                '\n11) Household_goods;' \
                '\n12) Transport;' \

CATEGORIES = ('donation', 'salary', 'mts_piggybank', 'other', 'medicines', 'rent',
              'food', 'phone', 'clothes', 'subscriptions', 'household_goods', 'transport')


def is_correct_format(splitted_message: list[str]) -> bool:
    condition_1 = len(splitted_message) == 4
    if condition_1:
        condition_2 = splitted_message[0].lower() in CATEGORIES
        condition_3 = splitted_message[1].lower() in ('да', 'нет')
        condition_4 = splitted_message[3].isdigit()
        return all([condition_2, condition_3, condition_4])
    return False


def check_end_of_month(month, year):
    if month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31

