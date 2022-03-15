# Deposit calculation service

Deposit calculation service - это приложение, написанное на фреймворке Flask. Данное приложение может рассчитывать сложный процент по вкладу(депозиту) сроком до 5 лет (60 месяцев)


## How to use

Для использования данного сервиса нужно отправить POST запрос Flask приложению на эндпоинт `/deposit_calc` следующего типа:
```
{
    "date": "Дата формата dd.mm.YYYY",
    "periods": Количество месяцев по вкладу (до 60) (int),
    "amount": Стартовая сумма вклада от 10 000 до 3 000 000 (int),
    "rate": Годовая ставка по вкладу от 1 до 8 процентов (float)
}
```
Более подробно схему валидации можно увидеть в данном репозитории по адресу `schemas/DepositCalcSchema.json`.

В случае конкретного запроса, от приложения последует JSON ответ следующего типа:
```
{
    "31.01.2021": 10050.0,
    "28.02.2021": 10100.25,
    "31.03.20221": 10150.75,
    ...
}
```
Если запрос не валидный, то пользователь получит JSON ответ с кодом 400:
```
{
    "error": "Описание ошибки"
}
```

## How to launch

Есть два варианта запуска этого приложения:

1. Запуск при помощи файла app.py
- Создание виртуального окружения
`python3 -m venv <Название виртуального окружения>`
- Активация виртуального окружения
`source <Название виртуального окружения>/bin/activate`
- Установка зависимостей
`pip3 install -r requirements.txt`
- Проведение тестов и получение отчета по ним
`coverage run -m unittest discover && coverage report -m`
- Запуск приложения
`python3 app.py`

2. Запуск в Docker контейнере из образа Dockerfile. В данном случае при сборке образа будут автоматически проведены тесты.
- Сборка Dokcer образа
`sudo docker build -t deposit_calculation:<tag> .`
- Запуск контейнера
`sudo docker run -p <Желаемый порт запуска>:5000 --name=deposit_calculation deposit_calculation:<tag>`
При добавлении флага `-d` к команде, контейнер будет запущен в фоновом режиме.

**Внимание!
Запуск приложения должен проводиться из корневой папки проекта.**

## Project Overview

- `app.py` - Основной файл, через который происходит запуск приложения, в нем заложен основной функционал Flask приложения
- `features.py` - Файл со вспомогательными функциями
- `logger.py` - Файл конфигурации логгера
- `settings.py` - Файл с настройками приложения
- `schemas` - Папка со JSON схемами валидации
- `tests` - Папка с unit тестами и тестовыми объектами
