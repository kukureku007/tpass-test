# Описание

Укорачиватель ссылок. Позволяет загрузить валидную url-ссылку и получить короткий хэш (длина хэша нового URL, указывается в файле settings.py в константе SHORT_URL_SIZE, по умолчанию равна 7), также сервис позволяет задать срок жизни ссылки в днях.

## Технологии
- Django
- Django REST Framework (DRF)
- gunicorn
- django-on-heroku (для деплоя на heroku)

## Установка

Сервис готов к запуску на Heroku - (демо https://tpass-test.herokuapp.com/)

1. Установка зависимостей
2. Заполнение файла .env, согласно примеру - .env.template (Для использования Базы Данных PostgreSQL необходимо заполнить соответсвующие поля)
3. Запуск gunicorn url_shortener.wsgi

## Использование

1. Создать ссылку - POST-запрос к https://example.com/urls/ с JSON следующего вида. В ответ придёт JSON с полями slug (короткий URL) и expiration_date - дата, после которой ссылка перестанет быть актуальной.
```
{
    "origin": "https://example.com/to_redirect/",
    "days_to_expire": 3
}
```

2. Вывести все ссылки - GET-запрос к https://example.com/urls/
3. Для удаления ссылки необзодимо обратиться с запросом DELETE к эндпоинту https://example.com/urls/<int:n>/, где n - это id существующей ссылки.
4. Использование короткой ссылки, после создания короткой ссылки из п.1. будет получена модель с полем slug, допустим slug = SlUg123, тогда, короткую ссылку можно использовать следующим образом: https://example.com/SlUg123 - перейдя по данной ссылке, вы будете перенаправлены на указанную вами ссылку в п.1. в поле origin.
