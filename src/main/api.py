import datetime

from rest_framework import generics, response
from rest_framework.views import APIView
from django.db.models import Sum, QuerySet

from .models import Item
from .serializers import ItemCreateSerializer, ItemRetrieveSerializer
from .admin import check_end_of_month

EXPENSE_CATEGORIES = (
    'other', 'medicines', 'rent', 'food', 'phone', 'clothes', 'subscriptions', 'household_goods', 'transport'
)


class ItemFilters:

    @staticmethod
    def filter_expenses(start_date: datetime, end_date: datetime) -> int:
        expense = Item.objects.filter(is_expense=True, date__range=(start_date, end_date)).aggregate(
            Sum("amount"))['amount__sum']
        if expense is None:
            expense = 0
        return expense

    @staticmethod
    def filter_not_expenses(start_date: datetime, end_date: datetime) -> int:
        not_expense = Item.objects.filter(is_expense=False, date__range=(start_date, end_date)).aggregate(
            Sum("amount"))['amount__sum']
        if not_expense is None:
            not_expense = 0
        return not_expense

    @staticmethod
    def filter_by_categories(category: str, start_date: datetime, end_date: datetime) -> int:
        expense_by_category = Item.objects.filter(
                category=category, is_expense=True, date__range=(start_date, end_date)).aggregate(
                Sum("amount"))['amount__sum']
        if expense_by_category is None:
            expense_by_category = 0
        return expense_by_category


class CreateItemView(generics.CreateAPIView):

    serializer_class = ItemCreateSerializer
    queryset = Item.objects.all()


class RetrieveAllItemsView(generics.ListAPIView):

    serializer_class = ItemRetrieveSerializer
    queryset = Item.objects.all()


class ReportView(APIView):

    """Формирование отчета"""

    def post(self, request):
        month = int(request.data.get('month'))
        start_date = datetime.date(2022, month, 1)
        end_date = datetime.date(2022, month, check_end_of_month(month, 2022))
        total_expense = ItemFilters.filter_expenses(start_date=start_date, end_date=end_date)
        total_not_expense = ItemFilters.filter_not_expenses(start_date=start_date, end_date=end_date)
        total_diff = total_not_expense - total_expense
        final_response = {
            "Краткий отчет за месяц": {
                "Доход": total_not_expense,
                "Расход": total_expense,
                "Разница": total_diff,
            },
            "Отчет по категориям": {}
        }
        for category in EXPENSE_CATEGORIES:
            report_by_category = ItemFilters.filter_by_categories(
                category=category, start_date=start_date, end_date=end_date
            )
            final_response['Отчет по категориям'].update({category: report_by_category})
        return response.Response(final_response)
