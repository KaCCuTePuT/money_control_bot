## Бот для контроля расходов, написанный на Django и Aiogram.

***

### Dev версия бота, Polling.

### Реализовано в tg:
* Добавление статьи расхода/дохода
* Отправка отчет в tg
* Отправка отчета на почту
### Реализовано через админку Django:
* Добавление, удаление, редактирование статьи расходов/доходов


### Используемый стек на данный момент:
* Django
* DRF
* Sqlite(в будущем заменю на PostgreSQL)
* Celery, Redis

### Будет добавлено позже:
* Docker
* Prod версия будет переведена на webhook

Установка:
1) Склонировать репозиторий
2) Создать виртуальное окружение
3) После установки виртуального окружения нужно в файл 
`<название окружения>/bin/activate` добавить строчку 
`export PYTHONPATH="<путь до папки с проектом>"`
4) Установить зависимости `pip install -r req.txt`
5) Запустить сервер `python manage.py runserver`
6) Перейти в папку с ботом и запустить бота `python executor.py`
7) Запустить контейнер redis `docker run -d -p 6379:6379 --name redis redis`
8) Запустить celery worker `celery -A config worker -l INFO`
