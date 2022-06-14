import matplotlib.pyplot as plt


def draw_graph_common(message_dict: dict) -> None:
    """Создание диаграммы с тремя столбцами: доход, расход и разница"""
    left = [1, 2, 3]
    height = [
        message_dict['Краткий отчет за месяц']['Доход'],
        message_dict['Краткий отчет за месяц']['Расход'],
        message_dict['Краткий отчет за месяц']['Разница']
    ]
    tick_label = ['Доход', 'Расход', 'Разница']

    plt.bar(
        left, height, tick_label=tick_label, width=0.8, color=['green', 'red', 'green' if height[-1] > 0 else 'red']
    )

    plt.ylabel('Сумма, руб.')
    plt.title('Отчет за месяц')

    plt.savefig('report_common.pdf')


def draw_plot_by_categories(message_dict: dict) -> None:
    """Создание диаграммы РАСХОДОВ по категориям"""
    labels = ['other', 'medicines', 'rent', 'food', 'phone', 'clothes', 'subcriptions', 'household_goods', 'transport']
    sizes = [
        message_dict['Отчет по категориям']['other'],
        message_dict['Отчет по категориям']['medicines'],
        message_dict['Отчет по категориям']['rent'],
        message_dict['Отчет по категориям']['food'],
        message_dict['Отчет по категориям']['phone'],
        message_dict['Отчет по категориям']['clothes'],
        message_dict['Отчет по категориям']['subcriptions'],
        message_dict['Отчет по категориям']['household_goods'],
        message_dict['Отчет по категориям']['transport'],
    ]
    explode = (0 for x in range(1, 10))
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    plt.savefig('report_by_categories.pdf')
