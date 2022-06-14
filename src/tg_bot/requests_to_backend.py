import requests
import json

from diagram import draw_graph_common

from src.main.report_sending import send_report_on_email


def add_item(splitted_list: list[str]) -> None:
    """Отправка post запроса на добавление статьи расхода или дохода"""
    data = {
        "category": splitted_list[0].lower(),
        "is_expense":  splitted_list[0] == 'да',
        "description": ' '.join(splitted_list[2].split('_')),
        "amount": int(splitted_list[3])
    }
    r = requests.post('http://127.0.0.1:8000/api/create', data=data)


def show_report(month: int) -> str:
    """Отправка post запроса на вывод отчета в tg"""
    data = {
        "month": month
    }
    r = requests.post('http://127.0.0.1:8000/api/report', data=data)
    message_text = json.loads(r.text)
    draw_graph_common(message_text)
    message_answer = f"Доход: {message_text['Краткий отчет за месяц']['Доход']}," \
                     f"\nРасход: {message_text['Краткий отчет за месяц']['Расход']}," \
                     f"\nРазница: {message_text['Краткий отчет за месяц']['Разница']}."
    return message_answer


def send_report(month: int) -> str:
    """Отправка post запроса на отправку отчета на почту"""
    report = show_report(month)
    send_report_on_email(month, report)
    return 'Отчет отправил, проверяй'
