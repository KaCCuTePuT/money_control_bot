import datetime

from django.contrib import admin
from django.db.models import Avg, Sum

from .models import Item
from src.utils import check_end_of_month


def total(is_expense, start_date, end_date):
    result = Item.objects.filter(is_expense=is_expense, date__range=(start_date, end_date)).aggregate(Sum("amount"))
    return result['amount__sum'] if result['amount__sum'] else 0


class ItemAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'is_expense', 'date', 'show_total', 'show_diff')
    list_filter = ('category', 'is_expense')
    date_hierarchy = 'date'

    def show_total(self, obj):
        start_date = datetime.date(obj.date.year, obj.date.month, 1)
        end_date = datetime.date(obj.date.year, obj.date.month, check_end_of_month(obj.date.month, obj.date.year))
        return total(is_expense=obj.is_expense, start_date=start_date, end_date=end_date)

    def show_diff(self, obj):
        start_date = datetime.date(obj.date.year, obj.date.month, 1)
        end_date = datetime.date(obj.date.year, obj.date.month, check_end_of_month(obj.date.month, obj.date.year))
        return total(
            is_expense=False, start_date=start_date, end_date=end_date
        ) - total(
            is_expense=True, start_date=start_date, end_date=end_date
        )


admin.site.register(Item, ItemAdmin)
