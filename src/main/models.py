from django.db import models
from django.utils.timezone import now

CATEGORIES = [
    ('donation', 'Плазмосдача'),
    ('salary', 'Зарплата'),
    ('mts_piggybank', 'Копилка МТС'),
    ('other', 'Прочее'),
    ('medicines', 'Лекарства'),
    ('rent', 'Аренда'),
    ('food', 'Еда'),
    ('phone', 'Телефон'),
    ('clothes', 'Одежда'),
    ('subscriptions', 'Подписки, донаты и т.д.'),
    ('household goods', 'Товары для быта и гигиены'),
    ('transport', 'Транспорт')
]


class Item(models.Model):
    description = models.TextField('Описание')
    is_expense = models.BooleanField('Расход?', default=True)
    category = models.CharField('Категория', choices=CATEGORIES, max_length=100)
    date = models.DateField('Дата', default=now)
    amount = models.IntegerField('Сумма')

    def __str__(self):
        return f'{self.category} - {self.description} - {self.amount}'

    class Meta:
        ordering = ('-date', 'is_expense')
