from django.urls import path
from . import api

urlpatterns = [
    path('create', api.CreateItemView.as_view()),
    path('all', api.RetrieveAllItemsView.as_view()),
    path('report', api.ReportView.as_view()),
]